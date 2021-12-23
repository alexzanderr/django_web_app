

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseNotFound
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.http import SimpleCookie

from django.shortcuts import render
# this is for filter function
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404


from . import models


def learning_index(request: HttpRequest):
	return render(request, "learning_index.html", {
		"title": "learning"
	})




def learning_error(request: HttpRequest):
	# asta da exception si este handled de django
	# si se duce la functia de jos .. 'learning_custom_404_page'
	raise Http404("this is an error from andrew")
	return HttpResponseNotFound('how about this')


def learning_custom_404_page(
	request: HttpRequest,
	exception=None
):
	try:
		print("error", str(exception))
	except Exception:
		pass
	# print(exception)
	return render(request, "errors/404.html", {})


def learning_ln(request):
	return render(request, "learning/test.html", {})

from django.views import generic

class TestView(generic.ListView):""