

from django.urls import path, include

from . import views


# url patterns for
urlpatterns = [

    # /todos/api
    path("", views.todos_api_index, name='todos_api_index'),

    # /todos/api/register/validation/
    path(
    	"register/validation",
    	views.TodosAPIRegisterValidation.as_view(),
    	name='todos_api_register_validation'
    ),
    # /todos/api/register/validation/username
    path(
        "register/validation/username",
        views.TodosAPIRegisterValidationUsername.as_view(),
    ),
    # /todos/api/mongo/add
    path("mongo/add", views.todos_api_mongo_add, name='todos_api_mongo_add'),
    # /todos/api/mongo/complete
    path("mongo/complete", views.todos_api_mongo_complete, name='todos_api_mongo_complete'),
    # /todos/api/mongo/delete
    path("mongo/delete", views.todos_api_mongo_delete, name='todos_api_mongo_delete'),

    # /todos/api/register/random/password
    path(
        "register/random/password",
        views.TodosAPIRegisterRandomPassword.as_view()
    )
]