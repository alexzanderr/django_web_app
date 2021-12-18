
# django modules
# from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
# from django.http import request
from django.http import JsonResponse
# from django.http import QueryDict
from django.views.decorators.http import require_http_methods

# python
import json
from datetime import datetime
from datetime import timedelta

# project
from mongo_client import Database
from mongo_client import ObjectId


@require_http_methods(["GET"])
def todos_api_index(request: HttpRequest):
    return JsonResponse(
        data={"message": "hello world from /todos/api"},
        status=200
    )


@require_http_methods(["POST"])
def todos_api_register_validation(request):
    return HttpResponse("its working from /todos/api/register/validation")


@require_http_methods(["POST"])
def todos_api_mongo_add(request: HttpResponse):
    request_body = json.loads(request.body)  # type: ignore
    todo = {
        "text": request_body["text"],  # type: ignore
        "timestamp": datetime.timestamp(datetime.now()),
        "datetime": datetime.now().strftime("%d.%m.%Y-%H:%M:%S"),
        "completed": False
    }
    Database.todos.insert_one(todo)
    # the above function insert a _id key

    todo["oid"] = str(todo["_id"])
    del todo["_id"]

    return JsonResponse(data=todo, status=200)



# PATCH request
# The PATCH method applies partial modifications to a resource
# meaning that in this case partial mods are todo completed == true
# /todos/api/mongo/complete
@require_http_methods(["PATCH"])
def todos_api_mongo_complete(request: HttpRequest):
    request_body = json.loads(request.body)  # type: ignore
    try:
        oid = request_body["oid"]
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e)}, status=500)  # type: ignore

    else:
        # execute if no exception
        requested_todo = Database.todos.find_one({
            "_id": ObjectId(oid)
        })
        completed = True
        if requested_todo["completed"]:  # type: ignore
            completed = False

        Database.todos.update_one(
            requested_todo,
            {"$set": {"completed": completed}}
        )
        requested_todo["oid"] = str(requested_todo["_id"])  # type: ignore
        requested_todo["completed"] = completed  # type: ignore

        del requested_todo["_id"]  # type: ignore

        return JsonResponse(requested_todo, status=200)  # type: ignore


# TODO add the oid in the post data body
# instead of making it an url, so that no one can see
# te oid
@require_http_methods(["DELETE"])
def todos_api_mongo_delete(request: HttpRequest):
    # if the client is sending data: JSON.stringify()
    request_body = json.loads(request.body)  # type: ignore

    try:
        oid = request_body["oid"]
    except Exception as e:
        print(e)
        return JsonResponse({"error": True}, status=500)  # type: ignore

    else:
        requested_todo = Database.todos.find_one({
            "_id": ObjectId(oid)
        })
        Database.todos.delete_one(requested_todo)
        requested_todo["oid"] = str(requested_todo["_id"])  # type: ignore
        del requested_todo["_id"]  # type: ignore

        return JsonResponse(requested_todo, status=200)  # type: ignore
