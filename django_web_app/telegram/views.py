
from django.http import HttpRequest
from django.http import HttpResponse

from django.shortcuts import render

def telegram_index(request: HttpRequest):
	return render(request, "telegram_index.html", {})
