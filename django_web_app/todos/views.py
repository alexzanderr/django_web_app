

from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from django.http import HttpRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


import sys
sys.path.append("..")
from mongo_client import Database



# GET /todos
def todos_index(request):
	todo_list = []
	for todo in Database.todos.find():
		todo["oid"] = todo["_id"]
		del todo["_id"]
		todo_list.append(todo)

	return render(request, "todos_index.html", {
		"todo_list": todo_list
	})


# GET /todos/agent
def todos_agent(request: HttpRequest):
	user_agent = request.headers['User-Agent'] # type: ignore
	# do something based on user agent
	return HttpResponse(user_agent)


def todos_mongo_test(request):
	return JsonResponse(
		data=Database.todos.find_one({
			"_id": "61ba5667de8183a2824bfb9d"}),
		safe=False
	)

def todos_testing(request):
	return render(request, "testing.html", {
		"variable": "john"
	})


def todos_extender(request):
	return render(request, "extender.html")


# GET /todos/json
@require_http_methods(["GET"])
def todos_json(request: HttpRequest):
	return JsonResponse({
		"message": "hello andrew"
	})



# GET /todos/register
# POST /todos/register
@require_http_methods(["GET", "POST"])
def todos_register(request: HttpRequest):
	"""
	Function: todos_register
	Summary:
		if get returns register page;
		if post then register's user with register jwt token
	Attributes:
		@param (request:HttpRequest):InsertHere
	"""
	if request.method == "GET":
		return render(request, "register.html")

	elif request.method == "POST":
		username = request.POST.get("username", None)
		password = request.POST.get("password", None)
		email = request.POST.get("email", None)
		register_token = request.POST.get("register_token", None)

		# do something with these items

	return JsonResponse({"message": "hello andrew"})




def todos_flask(request: HttpRequest):
	for item in Database.todos.find():
		return JsonResponse({"message": item["text"]})