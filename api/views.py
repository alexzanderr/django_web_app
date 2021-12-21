
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework import permissions


from .models import AuthToken

from mongo_client import Database
from views_enhanced import json_response

# https://stackoverflow.com/questions/31335736/cannot-apply-djangomodelpermissions-on-a-view-that-does-not-have-queryset-pro

from random import choice, randint
from string import ascii_letters, digits

def generate_random_token():
    return "".join([choice(ascii_letters + digits) for _ in range(30)])


# GET /api/
@api_view(["GET"])
# TODO fix permissions in production
@permission_classes((permissions.AllowAny,))
def api_index(request: HttpRequest):
    return JsonResponse({
        "message": "rest api its working"
    }, status=200)


# GET /api/todos
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


# GET /api/login
# GET /api/login?token=aopshnfasopbfhaujisbfiobhuj
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def api_login(request: HttpRequest):
    url_token = request.GET.get("token")
    if not url_token:
        return json_response({
            "message": "forbidden, you must provide ?token",
            "code": 403
        }, 403)

    database_token = AuthToken.objects.filter(token=url_token).first()
    if not database_token:
        return json_response({
            "message": "invalid token",
            "code": 403
        }, 403)

    return json_response({
        "message": f"you are now logged in with token: {url_token}",
        "code": 200
    }, 200)


# GET /api/new_token
# GET /api/new_token?name=aopshnfasopbfhaujisbfiobhuj
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def api_new_token(request: HttpRequest):
    new_token = request.GET.get("name")
    database_token = AuthToken.objects.filter(token=new_token).first()

    if database_token:
        return json_response({
            "message": "token already in database, sorry",
            "code": 403
        }, 403)

    return json_response({
        "message": f"you generated new token: {new_token}",
        "code": 200
    }, 200)