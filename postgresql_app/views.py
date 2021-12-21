"""
	just a small docstring for this module
	sublime text is great and its very fast
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import request
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import transaction

from .models import Club

from views_enhanced import json_response




def postgres_index(request) -> JsonResponse:
	return json_response({
		"message": "postgresql its working"
	})



@require_http_methods(["GET"])
def postgres_add_club(request: HttpRequest):
	name = request.GET.get("name", None)
	address = request.GET.get("address", None)
	if name and address:
		Club.objects.create(name=name, address=address)
		# new_club = Club(name=name, address=address)
		# new_club.save()

		return json_response({
			"message": "successfully added new club to database",
			"club": {
				"id": new_club.id, # type: ignore
				"name": name,
				"address": address
			},
		})

	return json_response({
		"message": "you must provide some details in the url like /postgres/add/club?name=test&address=test",
		"disclaimer": "this endpoint is experimental and for educational purpose only, DONT use this in production"
	}, 403)

# to remove

# new

@require_http_methods(["GET"])
def postgres_list_club(request):
	clubs = { "clubs": [] }

	for club in Club.objects.all(): # type: ignore
		clubs["clubs"].append({"id": club.id, "name": club.name, "address": club.address})
	return json_response(clubs)


@require_http_methods(["GET"])
def postgres_get_club(request, primary_key):
	club = Club.objects.get(pk=primary_key) # type: ignore
	return json_response({
		"club": {
			"name": club.name,
			"address": club.address,
			"id": primary_key
	}})

@require_http_methods(["GET"])
def postgres_delete_club(request, primary_key):
	club = Club.objects.get(pk=primary_key) # type: ignore
	club.delete()
	return json_response({
		"club": {
			"name": club.name,
			"address": club.address,
			"id": primary_key
	}})




@require_http_methods(["GET"])
def postgres_update_club(request, primary_key):
	name = request.GET.get("name", None)
	address = request.GET.get("address", None)
	if name and address:
		club = Club.objects.get(pk=primary_key) # type: ignore
		club.name = name
		club.address = address
		club.save(update_fields=['name', "address"])

		return json_response({
			"club": {
				"name": club.name,
				"address": club.address,
				"id": primary_key
		}})

	return json_response({"message": "you must provide some data"}, 403)



