
from rest_framework.authtoken.models import Token
from .serializers import AuthTokenJSONSerializer
from .models import AuthToken
from views_enhanced import _patch
from views_enhanced import _delete
from views_enhanced import _get_post
from views_enhanced import _get

# special decorators made by author this project
from views_decorators import json_response_decorator
from views_decorators import json_api_response_decorator


from utilities import _get_conf
Configuration = _get_conf()

from string import ascii_letters, digits
from random import choice, randint
from mongo_client import Database
from rest_framework import status
from rest_framework.response import Response as APIResponse
from rest_framework.response import Serializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse

from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
_allow_any = (AllowAny,)


# https://stackoverflow.com/questions/31335736/cannot-apply-djangomodelpermissions-on-a-view-that-does-not-have-queryset-pro


from utilities import generate_random_token

# postgresql db -> django_web_app_postgresql_db
postgres = Configuration.Development.PostgreSQL.DATABASE_DJANGO


# current project


# GET /api/
# TODO fix permissions in production
@api_view(["GET"])
@permission_classes(_allow_any)
@json_response_decorator
def api_index(request: HttpRequest):
    return {
        "message": "rest api its working"
    }

# GET /api/todos
@api_view(["GET"])
@permission_classes(_allow_any)
@json_response_decorator
def api_todos(request: HttpRequest):
    # lists todos
    todo_list = []
    for todo in Database.todos.find():
        todo["oid"] = str(todo["_id"])
        del todo["_id"]
        print(todo)
        todo_list.append(todo)

    return {
        "todos": todo_list
    }


from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

class AuthTokenViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = AuthToken.tokens.all()
    serializer_class = AuthTokenJSONSerializer

    # this are standard functions for ModelViewSet
    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

    # you dont even need to define this
    # because its handled automatically
    # you define this if you want custom output
    @json_api_response_decorator
    def list(self, request: HttpRequest):
        tokens = AuthToken.tokens.all()
        return {
            "status": 200,
            "tokens": AuthTokenJSONSerializer(tokens, many=True).data
        }

    # @json_api_response_decorator
    def retrieve(self, request, pk=None):
        _all = AuthToken.tokens.all()
        token = get_object_or_404(_all, pk=pk)
        return Response({
            "status": 200,
            "token": AuthTokenJSONSerializer(token).data
        })


# GET /api/postgres/tokens
# TODO make the decorator for the entire class, is it possible?
class PostgresTokensView(APIView):
    permission_classes = _allow_any

    # GET /api/postgres/tokens
    @json_api_response_decorator
    def get(self,
            request: HttpRequest,
            primary_key: int = None
            ):
        if primary_key:
            token = AuthToken.tokens.get_or_none(pk=primary_key)
            if token:
                _token = AuthTokenJSONSerializer(token).data
                return {
                    "status": 200,
                    "token": _token
                }

            return {
                "status": 404,
                "message": f"token with id: '{primary_key}' not found"
            },

        tokens = AuthToken.tokens.all()
        return {
            "status": 200,
            "tokens": AuthTokenJSONSerializer(tokens, many=True).data
        }


class TokenUtilities:
    def token_success_message(self, _token: AuthToken, **keyword_arguments):
        _json_resp = {
            "status": "success",
            "message": f"you generated this new token",
            "token": {
                "id": _token.id,  # type: ignore
                "value": _token.token
            },
            "code": 200
        }
        _json_resp.update(**keyword_arguments)
        return _json_resp

    def token_login_success_message(self, _token, **keyword_arguments):
        _json_resp = {
            "status": "success",
            "message": f"you are now logged in with token: {_token.token}",
            "code": 200
        }
        _json_resp.update(**keyword_arguments)
        return _json_resp

    def token_login_error_message(self, _token, **keyword_arguments):
        _json_resp = {
            "status": "error",
            "message": f"invalid token: {_token.token}",
            "code": 200
        }
        _json_resp.update(**keyword_arguments)
        return _json_resp

    def token_error_message(self, _token: AuthToken, **keyword_arguments):
        _json_resp = {
            "status": "error",
            "message": f"sorry, this token: '{_token.token}' is already in database",
            "token": {
                "id": _token.id,  # type: ignore
                "value": _token.token
            },
            "code": 403
        }
        _json_resp.update(**keyword_arguments)
        return _json_resp



# GET /api/postgres/tokens/new
# GET /api/postgres/tokens/new?value=aopshnfasopbfhaujisbfiobhuj
class PostgresNewTokenView(APIView, TokenUtilities):
    permission_classes = _allow_any

    def get(self, request: HttpRequest):
        new_token = request.GET.get("value")
        # return APIResponse({"value": new_token})
        if new_token:
            database_token = AuthToken.tokens.filter(token=new_token)

            if database_token:
                return json_api_response(
                    self.token_error_message(database_token[0]),
                    403)

            new_token = AuthToken.tokens.create(token=new_token)

            return json_api_response(
                self.token_success_message(new_token))

        random_new_token = generate_random_token()
        database_token = AuthToken.tokens.filter(token=random_new_token)  # type: ignore
        while database_token:
            random_new_token = generate_random_token()
            database_token = AuthToken.tokens.filter(token=random_new_token)  # type: ignore

        new_token = AuthToken.tokens.create(token=random_new_token)

        return json_api_response(
            self.token_success_message(new_token))




import json

# GET /api/login (browser request)
# GET /api/login (ajax request)
# GET /api/login?token=aopshnfasopbfhaujisbfiobhuj (browser request)
class APILoginView(APIView, TokenUtilities):
    permission_classes = _allow_any

    def get_request_origin(self, request: HttpRequest):
        return request.is_ajax()


    def get(self, request: HttpRequest):
        _ajax_request = True if request.is_ajax() else False
        _request_origin = "request made from AJAX" if _ajax_request else "requrest made from browser"

        if _ajax_request:
            json_body = json.loads(request.body)
            try:
                url_token = json_body["url_token"]
            except (KeyError, Exception) as error:
                return json_api_response({
                    "status": "error",
                    "message": "looks like you need to provide the token in AJAX body",
                    "error": str(error)
                })
            else:
                return url_token

        url_token = request.GET.get("token")
        if not url_token:
            return json_api_response({
                "status": "error",
                "message": "forbidden, you must provide ?token",
                "extra": _request_origin,
                "code": 403
            }, 403)



        database_token = AuthToken.tokens.filter(token=url_token)
        if not database_token:
            return json_api_response({
                "status": "error",
                "message": f"invalid token: {url_token}",
                "extra": _request_origin,
                "code": 403
            }, 403)

        return json_api_response({
            "status": "success",
            "message": f"you are now logged in with token: {url_token}",
            "extra": _request_origin,
            "code": 200
        }, 200)


# @api_view(_get)
# @permission_classes(_allow_any)
# def api_new_token_from_model(request):
#     token = Token.objects.create(user=...)
#     print(token.key)


@api_view(_get)
@permission_classes(_allow_any)
def api_error(r):
    raise ValueError("asd")



from todos.models import RegisterToken
from todos.serializers import RegisterTokenJSONSerializer
from datetime import datetime

def has_token_expired(_timestamp: float):
    return datetime.timestamp(datetime.now()) > _timestamp


@api_view(_get)
@permission_classes(_allow_any)
def api_todos_models_register_tokens_view(request, _id: int=None):
    # _all = RegisterToken.manager.create(token="random", expiration_timestamp=datetime.timestamp(datetime.now()))

    if _id:
        if not (0 < _id < len(RegisterToken.manager.all())):
            raise IndexError("_id must be between 0 and max contents")

        token = RegisterToken.manager.all()[_id]
        data = RegisterTokenJSONSerializer(token).data
        return json_api_response({"code": 200, "token": data})


    tokens = RegisterToken.manager.all()
    # print(tokens[0].expired)
    _json = RegisterTokenJSONSerializer(tokens, many=True)
    # print(_json)
    return json_api_response({"code": 200, "tokens": _json.data})

    # _token = AuthTokenJSONSerializer(token).data
    # print(token[0].id)
    # print(token[0]._id)
    # print(token[0].token)
    # print(token[0].expiration_timestamp)


from datetime import timedelta

@api_view(_get)
@permission_classes(_allow_any)
@json_api_response_decorator
def api_todos_models_register_tokens_new(request):
    new_token = RegisterToken.manager.create(
        token=generate_random_token(),
        expiration_timestamp=datetime.timestamp(
            datetime.now() + timedelta(minutes=5))
    )


    # _token = AuthTokenJSONSerializer(token).data
    # print(token[0].id)
    # print(token[0]._id)
    # print(token[0].token)
    # print(token[0].expiration_timestamp)
    data = RegisterTokenJSONSerializer(new_token).data
    return {"code": 200, "token": data}



@api_view(_get)
@permission_classes(_allow_any)
@json_api_response_decorator
def test_api_decorators(r):
    return {"data": 123}, 404



# GET /api/json-decorator-class
class TestJsonResponseDecorator(APIView):
    permission_classes = _allow_any

    @json_api_response_decorator
    def get(self, request: HttpRequest):
        return {
            "status": 200,
            "message": "it works"
        }