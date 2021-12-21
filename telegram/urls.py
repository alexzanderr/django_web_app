



from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	# /telegram/
    path("", views.telegram_index, name="telegram_index"),
]
