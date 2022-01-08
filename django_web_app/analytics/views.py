
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


from views_enhanced import *
# Create your views here.


from .models import TodosVisitCount

def index(r):
    return HttpResponse("index of analytics")


def analytics_todos(request: HttpRequest):
    total_visits = TodosVisitCount.manager.get_total_visits()
    return HttpResponse(f"total visits for /todos: {total_visits}")