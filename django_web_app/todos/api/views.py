
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


# TODO fix the below items

def generate_random_register_token():
    return "".join([choice(ascii_letters + digits) for _ in range(30)])


def get_new_register_token():
    """
    Function: get_new_token()
    Summary: gets new token based on whats in the db
    Returns: new token that is not the database
    """
    brand_new_token = generate_random_register_token()

    while register_tokens_collection.find_one({"token": brand_new_token}):
        brand_new_token = generate_random_register_token()

    return brand_new_token


@todos.route("/register", methods=["GET", "POST"])
def todos_register():
    method = request.method
    if method == "POST":
        # then create a new user in database and encrypt
        # the password
        # then redirect to /todos based on the content that the user has in todos database
        # return render_template ?
        # get data and token from request data body
        json_from_request: dict = request.get_json()  # type: ignore
        username = json_from_request["username"]
        email = json_from_request["email"]
        password = json_from_request["password"]
        password_check = json_from_request["password_check"]
        remember_me = json_from_request["remember_me"]
        register_token = json_from_request["register_token"]

        if not register_tokens_collection.find_one({"token": register_token}):
            return {
                "message": "cannot register, register token is not database"
            }, 403

        users_collection.insert_one({
            "username": username,
            "password": hash_password(password),  # hashed
            "email": email,
            "creation_timestamp": datetime.timestamp(datetime.now()),
            "creation_datetime": datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
        })

        # you can redirect from POST request sorry
        # and you can render HTML from here because you
        # are making the request from ajax, not from firefox
        return {"message": "success", "redirectTo": "/todos"}, 200
        # or you can redirect to login page
        # or you can automatically login the user after registration

    else:
        # GET
        # if the user is already authenticated
        # then redirect to /todos page
        # else
        # return below
        return render_template("todos/register.html")


@todos_api.post("/register/validation")
def todos_api_register():
    """
            Function: todos_api_register
            Returns: json with validated input
    """
    json_from_request: dict = request.get_json()  # type: ignore
    username = json_from_request["username"]
    email = json_from_request["email"]
    password = json_from_request["password"]
    password_check = json_from_request["password_check"]
    remember_me = json_from_request["remember_me"]

    # some examples
    results = {
        "username": validate_username(username),
        "password": validate_password(password),
        "email": validate_email(email),
        "password_check": validate_password_check(password, password_check),
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
        register_tokens_collection.insert_one({
            "token": new_token,
            "expiration_timestamp": datetime.timestamp(datetime.now() + timedelta(minutes=2))
        })

    # TODO add check for username in database

    return json_response(results, 200)
    # return {
    #   "username": username,
    #   "email": email,
    #   "password": password,
    #   "password_check": password_check,
    #   "remember_me": remember_me
    # }, 200
