from rest_framework import serializers

from . import models

# Serializers goes here


# Like Serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = "__all__"
        extra_kwargs = {
            "profile": {"read_only": True},
            "post": {"read_only": True},
        }


# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = models.Post
        fields = "__all__"
        extra_kwargs = {
            "profile": {"read_only": True},
            "author": {"read_only": True},
        }

    def get_likes(self, instance):
        return instance.like_set.count()
