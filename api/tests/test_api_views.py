


from django.test.client import Client as DjangoClient
import json

def test_api_index_view(client: DjangoClient):
	# this must be nammed 'client' otherwise its not going to work
	resp = client.get("/api/")
	assert resp.json() == {"message": "rest api its working"}
	print("REST API its working")



def test_api_todos_view(client: DjangoClient):
	resp = client.get("/api/todos")
	_json = resp.json()
	assert isinstance(_json, dict)
	print("/api/todos its working")