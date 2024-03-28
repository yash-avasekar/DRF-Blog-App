from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from .permissions import IsOwnerOrReadOnly

# Create your views here.


# Post Viewsets
class PostViewset(viewsets.ModelViewSet):
    """
    Post Viewset
    - List ,Create ,Update ,Delete
    """

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=request.user.profile, author=request.user.first_name)
        print("*" * 50)
        print(request.user.first_name)
        print("*" * 50)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        methods=["post"],
        serializer_class=serializers.LikeSerializer,
        permission_classes=[IsAuthenticated],
    )
    def like_or_unlike(self, request, pk=None):
        is_liked = models.Like.objects.filter(
            profile=request.user.profile, post=self.get_object()
        ).exists()

        if is_liked:
            models.Like.objects.filter(
                profile=request.user.profile, post=self.get_object()
            ).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=request.user.profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
