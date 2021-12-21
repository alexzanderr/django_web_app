

class Configuration:
    """
            The development server is where you work. ... The staging server is where you deploy your work for folks to look at - before it goes to production. Think of it as the place you show your client your work.
    """
    class Development:
        SECRET_KEY = 'not a real key'
        DEBUG = True

        # postgresql uri
        SQLALCHEMY_DATABASE_URI = "postgresql://username@host/database"

        class PostgreSQL:
            USERNAME = "username"
            PASSWORD = "password"
            HOST = "localhost"
            PORT = "5432"
            DATABASE_DJANGO = "database"
            POSTGRESQL_CONNECTION_STRING = f"postgresql://{USERNAME}@{HOST}/{DATABASE_DJANGO}"

        # how to use this key
        # curl -H "Authorization: Bearer {key}" http://localhost:3000/api/dashboards/home
        GRAFANA_API_KEY = "very long key for grafana"

        # https://pythonhosted.org/Flask-MongoAlchemy/#api
        # this is for mongo alchemy (stupid module)
        MONGODB_DATABASE_FLASK = "database_flask"
        MONGODB_DATABASE_DJANGO = "database_django"

        MONGODB_CONNECTION_STRING = "mongodb://username:password@localhost:27017"

        # this for flask-pymongo
        MONGO_URI_FLASK = "mongodb://username:password@localhost:27017/database_flask?authSource=admin"
        MONGO_URI_DJANGO = "mongodb://username:password@localhost:27017/database_django?authSource=admin"

        ALLOWED_HOSTS = [
            "127.0.0.1",
            "localhost",
            "*"
        ]

    class Staging(Development):
        pass

    class Production(Development):
        SECRET_KEY = "a_better_secret_key_for_production"
        DEBUG = False
        ALLOWED_HOSTS = [
            "0.0.0.0"
        ]