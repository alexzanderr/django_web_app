
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler403


from . import views


app_name = 'learning'

urlpatterns = [
    # /learning
    path("", views.learning_index, name="learning_index"),
    # /learning/error
    path("error", views.learning_error, name="learning_error"),
    # /learning/error2
    path("error2", views.learning_custom_404_page, name="learning_custom_404_page"),

    # /learning/ln
    path("ln", views.learning_ln, name="learning_ln"),

    # /viewcount
    path("viewcount", views.PageViewCounter.as_view()),


]
