



from .models import RegisterToken
from .models import mondels
from rest_framework import serializers

class RegisterTokenJSONSerializer(serializers.ModelSerializer):
    _id = mondels.ObjectIdField()
    token = serializers.CharField(max_length=100)
    expiration_timestamp = serializers.FloatField()
    expired = serializers.BooleanField()

    class Meta:
        model = RegisterToken
        fields = ("_id", "token", "expiration_timestamp", "expired")
