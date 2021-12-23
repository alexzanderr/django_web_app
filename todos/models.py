

from djongo import models


class Todo(models.Model):
    text = models.CharField(max_length=100) # type: ignore
    # completed = models.BoolField(default=False) # type: ignore