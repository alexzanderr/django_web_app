

class Configuration:
    """
            The development server is where you work. ... The staging server is where you deploy your work for folks to look at - before it goes to production. Think of it as the place you show your client your work.
    """
    class Development:
        SECRET_KEY = 'not a real key'
        REMOTE_DATABASES = False
        DEBUG = True


        # postgresql uri
        SQLALCHEMY_DATABASE_URI = ""

        class MySQL:

            class Cloud:
                USERNAME = ""
                PASSWORD = ""
                HOST = ""
                PORT = 25060
                DATABASE = ""
                SSLMODE = ""

            USERNAME = ""
            PASSWORD = ""
            HOST = ""
            PORT = ""
            DATABASE_DJANGO = ""

        class PostgreSQL:

            class Cloud:
                USERNAME = ""
                PASSWORD = ""
                HOST = ""
                # PORT =
                DATABASE = ""
                CONNECTION_STRING = f""

            USERNAME = ""
            PASSWORD = ""
            HOST = ""
            PORT = ""
            DATABASE_DJANGO = ""
            DATABASE_AUTH = ""
            POSTGRESQL_CONNECTION_STRING = f""

        GRAFANA_API_KEY = ""

        class MongoDB:
            DATABASE_DJANGO = ""
            USERNAME = ""
            PASSWORD = ""
            HOST = ""
            PORT = 27017
            AUTHSOURCE = ""

            MONGODB_CONNECTION_STRING = ""
            MONGO_URI_DJANGO = ""

            class Cloud:
                """
                    here are credentials for mongo in cloud
                """
                USERNAME = ""
                PASSWORD = ""
                CLUSTER = ""
                DATABASE = ""
                HOST = f""
                PORT = 27016
                CONNECTION_STRING = f""


        # https://pythonhosted.org/Flask-MongoAlchemy/#api
        # this is for mongo alchemy (stupid module)
        MONGODB_DATABASE_FLASK = ""
        MONGODB_DATABASE_DJANGO = ""

        MONGODB_CONNECTION_STRING = ""

        # this for flask-pymongo
        MONGO_URI_FLASK = ""
        MONGO_URI_DJANGO = ""

        ALLOWED_HOSTS = [
            "*"
        ]

        class Sentry:
            # data source
            DSN = ""


    class Staging(Development):
        pass

    class Production(Development):
        SECRET_KEY = "a_better_secret_key_for_production"
        DEBUG = False
        ALLOWED_HOSTS = [
            "0.0.0.0"
        ]