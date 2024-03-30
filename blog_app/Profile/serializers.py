from rest_framework import serializers

from . import models

# Serializers goes here


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }


# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = "__all__"

    def validate_username(self, value):

        if " " in value:
            raise serializers.ValidationError("Username cannot contain spaces.")

        if not value.islower():
            raise serializers.ValidationError("Username must be all lowercase.")

        return value

    def get_posts_count(self, instance):
        return instance.Post.count()
