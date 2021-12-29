
from django.db import models

from credentials import Configuration

_mysql_database = Configuration.Development.MySQL.DATABASE_DJANGO




class MySQLModel(models.Model):
    # asta nu devine field pentru ca nu are clasa de model.Field
    # this cannot be __database because django will ignore it
    _database = _mysql_database

    class Meta:
        abstract = True


from datetime import datetime

class TodosVisitCountManager(models.Manager):
    def get_queryset(self):
        _queryset = super().get_queryset()

        # if `_database` is set on model use that for choosing the DB
        if hasattr(self.model, "_database"):
            # the model that uses this manager
            # must have the attribute '_database'
            # in order to specify custom db
            _queryset = _queryset.using(self.model._database)

        return _queryset

    def create_default(self):
        return self.create(
            request_type="GET",
            timestamp=datetime.timestamp(datetime.now()),
            datetime=datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
        )

    def get_total_visits(self, **kwargs):
        try:
            # _all_visits = self.all()
            return len(self.all())
        except (KeyError, TodosVisitCount.DoesNotExist): # type: ignore
            return 0



class TodosVisitCount(MySQLModel):
    _route = "/todos"
    route = models.CharField(
        max_length=len(_route),
        default=_route)
    # get, post, update, delete, patch, put
    request_type = models.CharField(max_length=10)
    timestamp = models.FloatField()
    datetime = models.CharField(max_length=100)

    manager = TodosVisitCountManager()

    class Meta:
        db_table = "todos_route_visit_counts"



