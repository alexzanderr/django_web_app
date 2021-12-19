"""
	https://docs.djangoproject.com/en/4.0/topics/testing/tools/
"""

# same thing
# because client is in the __init__ of the test package
# from django.test import Client2
from django.test.client import Client as DjangoClient


def test_todos_index_view(client: DjangoClient):
	response = client.get("/todos/")
	# response.content is the html
	# print(response.content) # type: ignore
	assert response.status_code == 200 # type: ignore


def test_todos_json_view(client: DjangoClient):
	# aici trebuie sa fie /todos/json, nu /todos/json/
	# pentru ca json este ultimul din url
	response = client.get("/todos/json")
	# print(response.content)

	assert response.json() == {
		"message": "hello andrew"
	}