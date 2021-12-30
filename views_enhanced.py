"""
    this module is going to be used and usefull by all apps
"""


from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

from rest_framework.views import Response as APIResponse
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.status import HTTP_404_NOT_FOUND



_get = ["GET"]
_get_post = ["GET", "POST"]
_patch = ["PATCH"]
_delete = ["DELETE"]


def json_response(data: dict, status=200):
    return JsonResponse(data=data, status=status)


def json_response_decorator(_django_view_func):

    def inner_wrapper(*args, **kwargs):
        _returned = _django_view_func(*args, **kwargs)

        _data = {}
        _status_code = 200

        if isinstance(_returned, tuple):
            def validate_and_update_data():
                nonlocal _data
                __data: dict = _returned[0]
                if not isinstance(__data, dict):
                    raise TypeError(f"data must be dict. your data: {__data}")

                _data = __data

            if len(_returned) == 1:
                validate_and_update_data()

            elif len(_returned) == 2:
                # here must be status code
                __status_code: int = _returned[1]
                if not isinstance(__status_code, (str, int)):
                    raise TypeError(f"status code must be integer or string. your status code: {__status_code}")


                if not (99 < __status_code < 513):
                    raise ValueError(f"status code must be between 100 and 512. your status code: {__status_code}")

                _status_code = __status_code
                del __status_code


                validate_and_update_data()
        else:
            # _returned is dict type
            _data = _returned
            del _returned


        return json_response(_data, _status_code)
    return inner_wrapper


def json_api_response(data, status=HTTP_200_OK):
    return APIResponse(data=data, status=status)


class TemplateEngine:
    def __init__(self, appname) -> None:
        self.appname = appname


    def template(self, name):
        return f"{self.appname}/{name}"


    def index(self, request: HttpRequest, context={}) -> HttpResponse:
        return self.__render(request, "index.html", context=context)


    def __render(self, request: HttpRequest, template_name: str, context={}) -> HttpResponse:
        return render(request=request, template_name=self.template(template_name), context=context)


    def __call__(self, request: HttpRequest, template_name: str, context={}) -> HttpResponse:
        return render(request=request, template_name=self.template(template_name), context=context)


    def __str__(self) -> str:
        return f"<{TemplateEngine.__name__} appname: {self.appname}>"