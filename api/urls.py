
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	# /api/
    path("", views.api_index, name="api_index"),
	# /api/todos
    path("todos", views.api_todos, name="api_todos"),

    # /api/login?token=asijdgbaisdgbayhuisdyhuiavbgsdyhui -> OK
    # /api/login -> forbidden
    path("login", views.api_login, name="api_login"),

    # /api/new_token
    # /api/new_token?name=your_custom_token
    path("new_token", views.api_new_token, name="api_new_token"),
]
