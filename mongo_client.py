

from utilities import _get_conf
Configuration = _get_conf()

from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from pymongo.errors import InvalidOperation
from bson.objectid import ObjectId

_conn_string = Configuration.Development.MongoDB.MONGODB_CONNECTION_STRING
_db = Configuration.Development.MongoDB.DATABASE_DJANGO

mongo_db_client = MongoClient(_conn_string)
mongo_db_name = _db


class DatabaseDoesntExist(BaseException):
	pass

def get_mongo_client():
	return mongo_db_client



def database_exists(name: str):
	return name in mongo_db_client.list_database_names()

def get_database(name):
	if not database_exists(name):
		return DatabaseDoesntExist(f"database name: '{name}'")

	return mongo_db_client[name]


mongo_db = get_database(mongo_db_name)

def collection_exists(name:str, database=mongo_db):
	return name in database.list_collection_names() # type: ignore

def collection_create(name: str):
	"""
		Function: collection_create
		Summary: creates a mongo collection
		Examples: result = collection_create("todos")
		Attributes:
			@param (name):str
		Returns: True, if created successfully or raises CollectionInvalid error because the collection already was in database
	"""
	if collection_exists(name):
		raise CollectionInvalid(
			f"collection with name: '{name}' already exists in database: '{mongo_db}'")


	mongo_db.create_collection(name) # type: ignore
	return True


def get_collection(name: str, database=mongo_db):
	if not collection_exists(name):
		raise CollectionInvalid(
			f"collection with name: {name} doesnt exist; "
			"use this code to create collection: "
			"'collection_create(\"{name}\")'"
		)

	return database.get_collection(name) # type: ignore


def create_or_get_collection(name: str):
	# if it doesnt exist, then create
	if not collection_exists(name):
		result = collection_create(name)
		if not result:
			raise ValueError(f"could not create collection: {name}")

	# then return the collection
	return get_collection(name)


class Database:
	todos_collection_name = "todos"
	todos = create_or_get_collection(todos_collection_name)

	users_collection_name = "users"
	users = create_or_get_collection(users_collection_name)

	register_tokens_collection_name = "register_tokens"
	register_tokens = create_or_get_collection(register_tokens_collection_name)


users_unique_keys = [{
    "name": "username",
    "exists": False
}]
for _, value in Database.users.index_information().items():
    for unique_key in value["key"]:
        for users_unique_key in users_unique_keys:
            if unique_key[0] == users_unique_key["name"]:
                users_unique_key["exists"] = True


for users_unique_key in users_unique_keys:
    if not users_unique_key["exists"]:
        Database.users.create_index([
            (users_unique_key["name"], 1)
        ], unique=True)



tokens_unique_keys = [{
    "name": "token",
    "exists": False
}]
for _, value in Database.register_tokens.index_information().items():
    for unique_key in value["key"]:
        for tokens_unique_key in tokens_unique_keys:
            if unique_key[0] == tokens_unique_key["name"]:
                tokens_unique_key["exists"] = True


for tokens_unique_key in tokens_unique_keys:
    if not tokens_unique_key["exists"]:
        Database.register_tokens.create_index([
            (tokens_unique_key["name"], 1)
        ], unique=True)
