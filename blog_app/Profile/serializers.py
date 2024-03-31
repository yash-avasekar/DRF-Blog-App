import re
from rest_framework import serializers
from django.contrib.auth import get_user_model

from . import models

# Serializers goes here

User = get_user_model()


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
    url = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = "__all__"

    def validate_username(self, value):
        """
        Validate the username field using Django's default username validators.
        """

        User._meta.get_field("username").clean(
            value, None
        )  # Use the default username validator
        return value

    def validate_email(self, value):
        """
        Validate the email field using Django's default email validators.
        """

        User._meta.get_field("email").clean(
            value, None
        )  # Use the default email validator
        return value

    def get_url(self, obj):
        """
        Get URL for profile routing
        """

        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(
                f"/api/user/profiles/{obj.username}/"
            )  # Assuming '/posts/' is the base URL for posts
        return ""

    def get_posts_count(self, instance):
        """
        Get the total no. of posts count of a profile
        """
        return instance.Post.count()
