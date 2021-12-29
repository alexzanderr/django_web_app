
from datetime import datetime
from djongo import models as mondels
from credentials import Configuration

from django.contrib import admin

_mongo_database = Configuration.Development.MongoDB.DATABASE_DJANGO
_auth_database = Configuration.Development.PostgreSQL.DATABASE_AUTH


# i dont think this is working
class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = _mongo_database

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class DjongoModel(mondels.Model):
    # asta nu devine field pentru ca nu are clasa de model.Field
    # this cannot be __database because django will ignore it
    _database = _mongo_database

    class Meta:
        abstract = True


from django.db.models.query import QuerySet

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


class RegisterTokenAdmin(MultiDBModelAdmin):
    pass


# class RegisterTokenQuerySet(QuerySet):
#     def get_non_expired(self):
#         """Filter out posts that aren't ready to be published"""
#         print()
#         return list(filter(lambda token: token.expired == False, self.all()))


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