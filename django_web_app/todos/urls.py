


from django.urls import path, include

from . import views


# url patterns for
# /todos
urlpatterns = [
    path("", views.todos_index, name='todos_index'),
    path("testing", views.todos_testing, name='todos_testing'),
    # /todos/extender
    path("extender", views.todos_extender, name='todos_extender'),
    # /todos/register
    path("register", views.todos_register, name='todos_register'),
    # /todos/json
    path("json", views.todos_json, name='todos_json'),
    path("agent", views.todos_agent, name='todos_agent'),

    # just testing the flask database (which had items before)
    # /todos/mongo/flask
    path("mongo/flask", views.todos_flask, name='todos_flask'),
    path("mongo/test", views.todos_mongo_test, name='todos_mongo_test'),

    # /todos/api/
    # you cant put slash here or anymore, it wont load
    # except this situation where you include another entire controller
    path("api/", include("todos.api.urls")),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]