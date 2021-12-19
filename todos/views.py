
# django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from django.http import HttpRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# python
from datetime import datetime

from mongo_client import Database



# GET /todos
def todos_index(request):
    todo_list = []
    for todo in Database.todos.find():
        todo["oid"] = str(todo["_id"])
        del todo["_id"]
        todo_list.append(todo)

    return render(request, "todos_index.html", {
        "todo_list": todo_list
    })


# GET /todos/agent
def todos_agent(request: HttpRequest):
    user_agent = request.headers['User-Agent'] # type: ignore
    # do something based on user agent
    return HttpResponse(user_agent)


def todos_mongo_test(request):
    return JsonResponse(
        data=Database.todos.find_one({
            "_id": "61ba5667de8183a2824bfb9d"}),
        safe=False,
        status=200
    )

def todos_testing(request):
    return render(request, "testing.html", {
        "variable": "john"
    })


def todos_extender(request):
    return render(request, "extender.html")


# GET /todos/json
@require_http_methods(["GET"])
def todos_json(request: HttpRequest):
    return JsonResponse({
        "message": "hello andrew"
    }, status=200)



def todos_flask(request: HttpRequest):
    for item in Database.todos.find():
        return JsonResponse({"message": item["text"]})






import json
import hashlib
from django.views import View

# GET /todos/register (login page)
# POST /todos/register (actual registration request)
class TodosRegister(View):
    """
    Function: todos_register
    Summary:
        if get returns register page;
        if post then register's user with register jwt token
    Attributes:
        @param (request:HttpRequest):InsertHere
    """

    def hash_password(self, password: str):
        # deci input pentru sha256 trebuie sa fie bytes
        return hashlib.sha256(password.encode()).hexdigest()


    def check_hash_of_password(self, username: str, password: str):
        _user = Database.users.find_one({"username": username})
        _hashed_password = self.hash_password(password)
        return _user["password"] == _hashed_password  # type: ignore


    # POST /todos/register (actual registration request)
    def post(self, request: HttpRequest):
        # 4jvndu__!@#qmgh49195AND
        json_body = json.loads(request.body)
        username = json_body["username"]
        password = json_body["password"]
        email = json_body["email"]
        register_token = json_body["register_token"]
        # print(username, password, email, register_token)

        if not Database.register_tokens.find_one({"token": register_token}): # type: ignore
            return JsonResponse({
                "message": "cannot register, register token is not database"
            }, status=403)

        Database.users.insert_one({
            "username": username, # type: ignore
            "password": self.hash_password(password), # type: ignore
            "email": email, # type: ignore
            "creation_timestamp": datetime.timestamp(datetime.now()),
            "creation_datetime": datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
        })

        # you cant redirect from POST request sorry
        # and you can render HTML from here because you
        # are making the request from ajax, not from firefox
        return JsonResponse({"message": "success", "redirectTo": "/todos"}, status=200)
        # or you can redirect to login page
        # or you can automatically login the user after registration

        # do something with these items

    # GET /todos/register (login page)
    def get(self, request: HttpRequest):
        return render(request, "register.html")





