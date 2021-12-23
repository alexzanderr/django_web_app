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