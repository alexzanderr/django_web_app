"""django_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # /
    path("", views.index, name="index"),
    # /routes
    path("routes", views.application_routes, name="application_routes"),
    # /routes/json
    path("routes/json", views.application_routes_json, name="application_routes_json"),

    # /todos
    # efectivelly include urls.py from todos folder
    path("todos/", include("todos.urls")),

    # how about /api, aici folosim django rest API
    path("api/", include("api.urls")),

    # /postgres
    path("postgres/", include("postgresql_app.urls")),
    # /context_menu
    path("context_menu", views.context_menu_index, name="context_menu_index"),
    # /admin
    path('admin/', admin.site.urls),
    # /telegram
    path('telegram/', include("telegram.urls")),
    # /learning
    path('learning/', include("learning.urls")),
]
