from rest_framework import serializers # type:ignore
from .models import User
from django.contrib.auth.hashers import make_password # type:ignore

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    # Hash the password before saving
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
