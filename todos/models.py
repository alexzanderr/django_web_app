
from datetime import datetime
from djongo import models as mondels
from credentials import Configuration

_mongo_database = Configuration.Development.MongoDB.DATABASE_DJANGO

class DjongoModel(mondels.Model):
    # asta nu devine field pentru ca nu are clasa de model.Field
    # this cannot be __database because django will ignore it
    _database = _mongo_database

    class Meta:
        abstract = True


class RegisterTokenManager(mondels.DjongoManager):

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
        except (KeyError, RegisterToken.DoesNotExist): # type: ignore
            return None



class RegisterToken(DjongoModel):
    _id = mondels.ObjectIdField()
    token = mondels.CharField(max_length=100) # type: ignore
    expiration_timestamp = mondels.FloatField() # type: ignore

    # completed = models.BoolField(default=False) # type: ignore

    manager = RegisterTokenManager()

    # this property is calculated at DB retreival
    # just after db fetch
    # this is run when querying from db
    @property
    def expired(self):
        # print(self._database)
        return datetime.timestamp(datetime.now()) > self.expiration_timestamp


    class Meta:
        db_table = "\"register_tokens_collection\""