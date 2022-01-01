

import pytest
import json
import logging
from django.test.client import Client as DjangoClient

def test_api_index_view(client: DjangoClient):
	# this must be nammed 'client' otherwise its not going to work
	resp = client.get("/api/")
	assert resp.json() == {"message": "rest api its working"}
	print("REST API its working")



def test_api_todos_view(client: DjangoClient, caplog):
	resp = client.get("/api/todos")
	caplog.set_level(logging.INFO)

	_json = resp.json()
	assert isinstance(_json, dict)
	print("/api/todos its working")

"""
-------------------------------- Captured stdout setup --------------------------------
Operations to perform:
  Synchronize unmigrated apps: application, debug_toolbar, django_extensions, livereload, messages, rest_framework, staticfiles
  Apply all migrations: admin, analytics, api, auth, authtoken, contenttypes, learning, mysql_remote, postgres_remote, postgresql_app, sessions, todos
Synchronizing apps without migrations:
  Creating tables...
    Creating table application_basemodel
    Creating table application_login
    Creating table application_user
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying analytics.0001_initial... OK
  Applying analytics.0002_auto_20211229_1553...
-------------------------------- Captured stderr setup --------------------------------
Creating test database for alias 'django_web_app_auth_db' ('test_django_web_app_auth_db')...
Got an error creating the test database: database "test_django_web_app_auth_db" already exists

Destroying old test database for alias 'django_web_app_auth_db' ('test_django_web_app_auth_db')...
"""
# yeah, same problem with database transactions
# this tells pytest to make db transactions (read, write) while testing
# @pytest.mark.django_db
# class TestRESTAPI:
# 	def test_api_todos_mongo_models_register_token(self, client: DjangoClient):
# 		resp = client.get("/api/todos/mongo/models/register_tokens")

# 		_json = resp.json()
# 		assert isinstance(_json, dict)
# 		assert _json["code"] == 200