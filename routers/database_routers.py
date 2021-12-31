
class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {
        'auth',
        'contenttypes',
        'sessions'
        'admin',
    }
    db_name = "django_web_app_auth_db"

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


class PostgresqlRouter:
    db_name = "django_web_app_postgresql_db"
    # this is used to tell django which models to use from which app (made by programmer or installed)
    route_app_labels = {

    }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


class RemotePostgresqlRouter:
    db_name = "tcbaekqa"
    # this is used to tell django which models to use from which app (made by programmer or installed)
    route_app_labels = {
        "postgres_remote"
    }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


class MongodbRouter:
    # this is the key from DATABASES dict from settings.py
    db_name = "django_web_app_mongo_db"
    route_app_labels = {}

    def db_for_read(self, model, **hints):
        database = getattr(model, '_database', None)
        if database:
            return database

        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        database = getattr(model, '_database', None)
        if database:
            return database

        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == self.db_name
        return None

class RemoteMongodbRouter:
    # this is the key from DATABASES dict from settings.py
    db_name = "django_web_app_mongo_db_remote"
    route_app_labels = {}

    def db_for_read(self, model, **hints):
        database = getattr(model, '_database', None)
        if database:
            return database

        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        database = getattr(model, '_database', None)
        if database:
            return database

        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


class MySQLRouter:
    # this is the key from DATABASES dict from settings.py
    db_name = "django_web_app_mysql_db"
    route_app_labels = {}

    def db_for_read(self, model, **hints):
        database = getattr(model, '_database', None)
        if database:
            return database

        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        database = getattr(model, '_database', None)
        if database:
            return database

        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


class RemoteMySQLRouter:
    # this is the key from DATABASES dict from settings.py
    db_name = "defaultdb"
    route_app_labels = {
        "mysql_remote"
    }


    x = 123
    def db_for_read(self, model, **hints):
        database = getattr(model, '_database', None)
        if database:
            return database

        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        database = getattr(model, '_database', None)
        if database:
            return database

        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == self.db_name
        return None
