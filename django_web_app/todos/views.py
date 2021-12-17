

from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.


def index(request):
	return HttpResponse("hello world from /todos")


def testing(request):
	return render(request, "testing.html", {
		"variable": "john"
	})


def extender(request):
	return render(request, "extender.html", {})