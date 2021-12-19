

from django.urls import path, include

from . import views


# url patterns for
# /todos/api
urlpatterns = [
    # you cant put slash here or anymore, it wont load
    path("", views.todos_api_index, name='todos_api_index'),
    path(
    	"register/validation",
    	views.TodosAPIRegisterValidation.as_view(),
    	name='todos_api_register_validation'
    ),
    # /todos/api/mongo/add
    path("mongo/add", views.todos_api_mongo_add, name='todos_api_mongo_add'),
    # /todos/api/mongo/complete
    path("mongo/complete", views.todos_api_mongo_complete, name='todos_api_mongo_complete'),
    path("mongo/delete", views.todos_api_mongo_delete, name='todos_api_mongo_delete'),
]