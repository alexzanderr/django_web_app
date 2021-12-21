
from django.http import HttpRequest
from django.http import HttpResponse

from django.shortcuts import render

def learning_index(request: HttpRequest):
	return render(request, "learning_index.html", {
		"title": "learning"
	})

def something():
	pass
