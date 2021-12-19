
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	# /api/
    path("", views.api_index, name="api_index"),
	# /api/todos
    path("todos", views.api_todos, name="api_todos"),
]
