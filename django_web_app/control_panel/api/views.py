

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import subprocess

from views_decorators import json_response_decorator

def focus_workspace(index):
    command = f"wmctrl -s {index}"
    subprocess.call(command, shell=True)


@json_response_decorator
def workspaces_index(request, index=None):
    if index:
        if not isinstance(index, int):
            return {"error": ""}

        if not (0 <= index <= 10):
            return {"error": "index must be between 0 and 10"}

        focus_workspace(index)
        

    return {"status": 200}
