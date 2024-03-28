from rest_framework import serializers

from . import models

# Serializers goes here


# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = "__all__"
        extra_kwargs = {
            "profile": {"read_only": True},
            "author": {"read_only": True},
        }


# Like Serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = "__all__"
        extra_kwargs = {
            "profile": {"read_only": True},
        }
