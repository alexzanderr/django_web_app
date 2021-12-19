
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework import permissions


from mongo_client import Database
from views_enhanced import json_response

# https://stackoverflow.com/questions/31335736/cannot-apply-djangomodelpermissions-on-a-view-that-does-not-have-queryset-pro

@api_view(["GET"])
# TODO fix permissions in production
@permission_classes((permissions.AllowAny,))
def api_index(request: HttpRequest):
    return JsonResponse({
        "message": "rest api its working"
    }, status=200)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def api_todos(request: HttpRequest):
    # lists todos
    todo_list = []
    for todo in Database.todos.find():
        todo["oid"] = str(todo["_id"])
        del todo["_id"]
        print(todo)
        todo_list.append(todo)

    return json_response({
        "todos": todo_list
    })

