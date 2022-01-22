


from django.contrib import admin
from django.urls import path
from django.conf.urls import handler403


from . import views


app_name = 'control_panel'

urlpatterns = [
    path("workspaces", views.workspaces_index),
    path("workspaces/<int:index>", views.workspaces_index),
]
