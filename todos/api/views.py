
# django modules
# from django.shortcuts import render
from django.views import View
import re
from string import ascii_letters, digits
from random import choice, randint
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

from views_enhanced import json_response


@require_http_methods(["GET"])
def todos_api_index(request: HttpRequest):
    return JsonResponse(
        data={"message": "hello world from /todos/api"},
        status=200
    )


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


def generate_random_register_token():
    return "".join([choice(ascii_letters + digits) for _ in range(30)])


def get_new_register_token():
    """
    Function: get_new_token()
    Summary: gets new token based on whats in the db
    Returns: new token that is not the database
    """
    brand_new_token = generate_random_register_token()

    while Database.register_tokens.find_one({"token": brand_new_token}):
        brand_new_token = generate_random_register_token()

    return brand_new_token

class ValidationUtilities():
    username_regex = re.compile("[a-zA-Z0-9_]+")
    password_regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})")
    email_regex = re.compile(r"[a-zA-Z0-9-.]+@[a-zA-Z0-9-.]+")

    def validate_username(self, username: str):

        if not isinstance(username, str):
            return {
                "passed": False,
                "error_message": "username is not a string"
            }

        len_username = len(username)
        if not (5 < len_username < 21):
            return {
                "passed": False,
                "error_message": "username must be between 6 and 20 characters"
            }

        if not self.username_regex.fullmatch(username):
            return {
                "passed": False,
                "error_message": "username must contain only alpha numeric values and underscore"
            }

        # deci testele au mers pana acum pentru
        # ca era mongo db involved aici
        if Database.users.find_one({"username": username}):
            return {
                "passed": False,
                "error_message": "username already exists"
            }

        return {
            "passed": True,
            "error_message": None
        }


    def validate_password(self, password: str):

        if not isinstance(password, str):
            return {
                "passed": False,
                "error_message": "password is not a string"
            }

        len_password = len(password)
        if not (9 < len_password < 41):
            return {
                "passed": False,
                "error_message": "password must be between 10 and 40 characters"
            }

        if not self.password_regex.match(password):
            return {
                "passed": False,
                "error_message": "password must contain alpha, digits, punctuation and uppercase"
            }

        return {
            "passed": True,
            "error_message": None
    }



    def validate_email(self, email: str):
        if not isinstance(email, str):
            return {
                "passed": False,
                "error_message": "password is not a string"
            }

        if "@" not in email:
            return {
                "passed": False,
                "error_message": "email doesnt contain '@'"
            }

        first, second = email.split("@")
        if not (5 <= len(first) <= 50):
            return {
                "passed": False,
                "error_message": "username from email must be between 5 and 50"
            }

        if not (5 <= len(second) <= 15):
            return {
                "passed": False,
                "error_message": "domain name from email must be between 5 and 15"
            }

        if not self.email_regex.fullmatch(email):
            return {
                "passed": False,
                "error_message": "regex resulted that email is invalid"
            }

        return {
            "passed": True,
            "error_message": None
        }

    def validate_password_check(self, password: str, password_check: str):
        if password_check != password:
            return {
                "passed": False,
                "error_message": "password doesnt match password check"
            }

        return {
            "passed": True,
            "error_message": None
        }


# POST /todos/api/register/validation
class TodosAPIRegisterValidation(View, ValidationUtilities):






    # POST /todos/api/register/validation
    def post(self, request: HttpRequest):
        """
                Function: todos_api_register
                Returns: json with validated input
        """
        # print(request.body)
        # print("username", request.POST.get("username"))

        try:
            if request.is_ajax():
                print("request is made from ajax (client) jquery")
                # here request is made from ajax with data == JSON.stringify(_json)
                json_from_request: dict = json.loads(request.body)  # type: ignore
                username = json_from_request["username"]
                email = json_from_request["email"]
                password = json_from_request["password"]
                password_check = json_from_request["password_check"]
                remember_me = json_from_request["remember_me"]

            else:
                print("request is made pytest-django-client")
                username = request.POST.get("username")
                email = request.POST.get("email")
                password = request.POST.get("password")
                password_check = request.POST.get("password_check")
                remember_me = request.POST.get("remember_me")

        except json.decoder.JSONDecodeError:
            # here request is made from pytest-django with post(url, data=_json)
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password_check = request.POST.get("password_check")
            remember_me = request.POST.get("remember_me")

        else:


            # some examples
            results = {
                "username": self.validate_username(username),
                "password": self.validate_password(password),
                "email": self.validate_email(email),

                "password_check": self.validate_password_check(password, password_check),
                "register_token": None
            }

            all_passed = True
            for k, v in results.items():
                if k != "register_token" and not v["passed"]:
                    all_passed = False
                    break

            if all_passed:
                new_token = get_new_register_token()
                results["register_token"] = new_token
                Database.register_tokens.insert_one({
                    "token": new_token,
                    "expiration_timestamp": datetime.timestamp(datetime.now() + timedelta(minutes=2))
                })

            return JsonResponse(results, status=200)


class TodosAPIRegisterValidationUsername(View, ValidationUtilities):
    def post(self, request: HttpRequest):
        if not request.is_ajax():
            return json_response({
                "message": "request must be from ajax"
                }, 403)

        json_from_request: dict = json.loads(request.body)  # type: ignore
        username = json_from_request["username"]
        return json_response({"username": self.validate_username(username)})