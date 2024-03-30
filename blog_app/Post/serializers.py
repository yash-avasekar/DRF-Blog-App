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
    url = serializers.SerializerMethodField()

    class Meta:
        model = models.Post
        fields = "__all__"
        extra_kwargs = {
            "profile": {"read_only": True},
            "author": {"read_only": True},
        }

    def get_likes(self, instance):
        return instance.like_set.count()

    def get_url(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(
                f"/api/posts/{obj.id}/"
            )  # Assuming '/posts/' is the base URL for posts
        return ""
