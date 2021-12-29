# """
#     https://docs.djangoproject.com/en/4.0/topics/testing/tools/
# """

# same thing
# because client is in the __init__ of the test package
# from django.test import Client2

from django.test.client import Client as DjangoClient
import json

def test_todos_api_index_view(client: DjangoClient):
    response = client.get("/todos/api/")
    # print(response)
    assert response.json() == {"message": "hello world from /todos/api"} # type: ignore
    # print(dir(response))
    # status code was 301 because the url should have '/todos/api/'
    # https://stackoverflow.com/questions/1579846/django-returning-http-301
    # to use this '/todos/api' you need to change APPEND_SLASH to True in settings.py (it doesnt work)
    assert response.status_code == 200 # type: ignore



def test_todos_api_register_validation_view_class(client: DjangoClient):
    # not valid because is in the database
    username = "miguel5000"
    # valid
    email = "just.an.email.test@gmail.com"
    password="123!@#asdASDdfognsofnjgdjofbgjodbfg"
    password_check="123!@#asdASDdfognsofnjgdjofbgjodbfg"
    remme = True
    _json = {
        "username": username,
        "email": email,
        "password": password,
        "password_check": password_check,
        "remember_me": remme
    }
    resp = client.post("/todos/api/register/validation", data=_json)
    assert resp.status_code == 200
    _json: dict = resp.json()

    # because in our database the username doesnt exists
    assert _json["username"]["passed"] == True, _json["username"]["error_message"]
    assert _json["username"]["error_message"] != "username already exists"




    # not valid because is in the database
    username = "miguel5000"
    # valid
    email = "just.an.email.test@gmail.com"
    password="123!@#asdASDdfognsofnjgdjofbgjodbfg"
    password_check="123!@#asdASDdfognsofnjgdjofbgjodbfg"
    remme = True
    _json = {
        "username": username,
        "email": email,
        "password": password,
        "password_check": password_check,
        "remember_me": remme
    }
    resp = client.post("/todos/api/register/validation", data=_json)
    assert resp.status_code == 200
    _json: dict = resp.json()

    # because in our database the username doesnt exist yet
    assert _json["username"]["passed"] == True
    # because the credentials are valid we get a register token
    assert _json["register_token"] != None

    print(_json)
    for k, value in _json.items():
        if k == "register_token":
            continue
        assert value["passed"] == True, value["error_message"]
