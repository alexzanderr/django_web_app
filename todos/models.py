

from djongo import models


class Todo(models.Model):
    text = models.CharField(max_length=100) # type: ignore
    # completed = models.BoolField(default=False) # type: ignore



from djongo import models as mondels
from credentials import Configuration


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


from datetime import datetime

class RegisterToken(mondels.Model):
    _database = Configuration.Development.MongoDB.DATABASE_DJANGO
    """
        >>> Person.objects.using("django_web_app_mongo_db")
        <QuerySet []>
        >>> Person.objects.using("django_web_app_mongo_db").filter()
        <QuerySet []>
        >>> Person.objects.using("django_web_app_mongo_db").create(name='andrew', age=21)
        <Person: Person object (61c4dee7cb56e2a9ac16069e)>
        >>> x = Person.objects.using("django_web_app_mongo_db").create(name='andrew', age=21)
        >>> x.id
        ObjectId('61c4df17cb56e2a9ac16069f')
        >>> x.name
        'andrew'
        >>> str(x.id)
        '61c4df17cb56e2a9ac16069f'
        >>> x.age
        21

        >>> x = Person.persons.create(name='andrewasdasdasd', age=21, last_name="sur", location="somewhere")
        >>> x
        <Person: Person object (61c4e1313593197ad3a92c66)>

          {
            _id: ObjectId("61c4e0fe12113572e268297f"),
            name: 'andrewasdasdasd',
            age: 21
          },
          {
            _id: ObjectId("61c4e1313593197ad3a92c66"),
            name: 'andrewasdasdasd',
            age: 21,
            last_name: 'sur',
            loc
        }

        look, mongo db is adjustable
    """
    _id = mondels.ObjectIdField()
    token = mondels.CharField(max_length=100) # type: ignore
    expiration_timestamp = mondels.FloatField() # type: ignore

    # completed = models.BoolField(default=False) # type: ignore

    manager = RegisterTokenManager()

    # this property is calculated at DB retreival
    # just after db fetch
    @property
    def expired(self):
        return datetime.timestamp(datetime.now()) > self.expiration_timestamp


    class Meta:
        db_table = "\"register_tokens_collection\""