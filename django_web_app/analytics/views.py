
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


from views_enhanced import *
from views_decorators import json_response_decorator


from .models import TodosVisitCount


def index(r):
    return HttpResponse("index of analytics")


@json_response_decorator
def analytics_todos(request: HttpRequest):
    total_visits = TodosVisitCount.manager.get_total_visits()
    return {
        "route": "/todos",
        "total": total_visits
    }


@json_response_decorator
def analytics_all_routes(request: HttpRequest):
    return {
        "visits": [
            {
                "route": "/todos",
                "total": analytics_todos(request)
            }
        ]
    }
