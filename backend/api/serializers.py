from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "password",
                  "last_name", "email", "is_active", "date_joined",)
        extra_kwargs = {"password": {"write_only": True, 'min_length': 8, }}
        read_only_fields = ("is_active", "date_joined")

    def validate(self, data):
        errors = dict()
        password = data.get("password")
        if len(password) < 8:
            errors["password"] = "Password must be at least 8 characters"
        if errors:
            raise serializers.ValidationError(errors)
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user