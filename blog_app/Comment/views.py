from rest_framework import viewsets, status
from rest_framework.response import Response

from . import models
from . import serializers
from .permissions import IsOwnerOfCommentOrOwnerOfPostOrReadOnly

# Create your views here.


# Comment Viewsets
class CommentViewsets(viewsets.ModelViewSet):
    """
    Comment Viewsets
    - List ,Create ,Update ,Delete
    """

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsOwnerOfCommentOrOwnerOfPostOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=request.user.profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
