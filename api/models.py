

from django.db import models
from credentials import Configuration



# class BaseModel(models.Model):
#     # __abstract__ = True
#     pass

# https://stackoverflow.com/questions/3519143/django-how-to-specify-a-database-for-a-model
class AuthTokenManager(models.Manager):
    def get_queryset(self):
        _queryset = super().get_queryset()

        # if `_database` is set on model use that for choosing the DB
        if hasattr(self.model, "_database"):
            # the model that uses this manager
            # must have the attribute '_database'
            # in order to specify custom db
            _queryset = _queryset.using(self.model._database)

        return _queryset

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except (KeyError, AuthToken.DoesNotExist): # type: ignore
            return None



class AuthToken(models.Model):
    _database = Configuration.Development.PostgreSQL.DATABASE_DJANGO
    # tablename = "auth_tokens"
    token = models.CharField(max_length=200)

    # call AuthTokens.tokens.all() instead of 'objects'
    # tokens = models.Manager()
    tokens = AuthTokenManager()

    # e problema mare cu init
    # def __init__(self, token: str):
    #     self.token = token

    def __str__(self):
        return f"<AuthToken token: {self.token}>"

    class Meta:
        # the name of the table in the actual database
        db_table = "\"auth_tokens_table\""


