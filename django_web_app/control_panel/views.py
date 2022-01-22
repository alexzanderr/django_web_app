
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import subprocess

# project
from views_decorators import json_response_decorator

@json_response_decorator
def index_json(request: HttpRequest):
    return {"status": "itsworking"}


def index(request: HttpRequest):
    return render(request, "control_panel/index.html")







