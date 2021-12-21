from django.contrib import admin

# Register your models here.
from . import models

# with this you can see your articles from the database
# in the admin interface and also you can create, update, read, delete
admin.site.register(models.Article)
