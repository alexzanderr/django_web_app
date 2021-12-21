

from django.db import models



class BaseModel(models.Model):
    # __abstract__ = True
    pass


class AuthToken(BaseModel):
    # tablename = "auth_tokens"
    token = models.CharField(max_length=100, unique=True)

    def __init__(self, token: str):
        self.token = token

    def __str__(self):
        return f"<AuthToken token: {self.token}>"