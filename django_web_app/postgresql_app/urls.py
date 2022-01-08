


from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	# /postgres/
    path("", views.postgres_index, name="postgres_index"),
	# /postgres/
    path("add/club", views.postgres_add_club, name="postgres_add_club"),
    path("list/club", views.postgres_list_club, name="postgres_list_club"),
    path("get/club/<int:primary_key>", views.postgres_get_club, name="postgres_get_club"),
    path("delete/club/<int:primary_key>", views.postgres_delete_club, name="postgres_delete_club"),
    path("update/club/<int:primary_key>", views.postgres_update_club, name="postgres_update_club"),
]
