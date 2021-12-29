
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler403


from . import views



urlpatterns = [
    # /analytics
    path("", views.index),
    # /analytics/todos
    path("todos/", views.analytics_todos)

]
