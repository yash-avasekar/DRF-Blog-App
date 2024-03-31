import re
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
    url = serializers.SerializerMethodField()
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

    def validate_email(self, value):
        """
        Validate the email field.
        """
        # Regular expression pattern to match the email format
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if value:
            # Check if the email matches the pattern
            if not re.match(pattern, value):
                raise serializers.ValidationError("Invalid email format")
            # Return the validated value
            return value
        raise serializers.ValidationError("Email cannot be null")

    def get_url(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(
                f"/api/user/profiles/{obj.username}/"
            )  # Assuming '/posts/' is the base URL for posts
        return ""

    def get_posts_count(self, instance):
        return instance.Post.count()
