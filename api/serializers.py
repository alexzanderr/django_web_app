

from .models import AuthToken
from rest_framework import serializers

class AuthTokenJSONSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=200)

    class Meta:
        model = AuthToken
        fields = ("__all__")
