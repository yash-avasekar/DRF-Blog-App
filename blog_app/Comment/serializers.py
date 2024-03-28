from rest_framework import serializers

from . import models

# Serializer goes here


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"
        extra_kwargs = {
            "profile": {"read_only": True},
            # "post": {"read_only": True},
        }
