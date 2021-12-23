
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
	# /api/
    path("", views.api_index, name="api_index"),
    # /api/tokens
    path("postgres/tokens/", views.PostgresTokensView.as_view(), name="postgres_tokens_view"),
    # /api/tokens/3
    path("postgres/tokens/<int:primary_key>", views.PostgresTokensView.as_view(), name="postgres_tokens_view_id"),

    # GET /api/postgres/tokens/new
    # GET /api/postgres/tokens/new?value=asdo123jfbiasdgbiyug23478
    path("postgres/tokens/new", views.PostgresNewTokenView.as_view(), name="postgres_new_token"),



	# /api/todos
    path("todos", views.api_todos, name="api_todos"),

    # /api/login?token=asijdgbaisdgbayhuisdyhuiavbgsdyhui -> OK
    # /api/login -> forbidden
    path("login", views.APILoginView.as_view(), name="api_login"),

    # /postgres
    # path("postgres", views.postgres, name="postgres"),
]