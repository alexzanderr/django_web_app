

from django.contrib import admin
from .models import RegisterToken
from .models import RegisterTokenAdmin


admin.site.register(RegisterToken, RegisterTokenAdmin)