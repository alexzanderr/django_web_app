
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler403

from django.urls import include

from . import views



urlpatterns = [
    # /learning
    path("", views.index, name="control_panel_index"),
    path("api/", include("control_panel.api.urls"))
]
