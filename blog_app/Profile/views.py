from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from . import models
from . import serializers
from . import utils
from .permissions import IsOwnerOrReadOnly
from Post.models import Post
from Post.serializers import PostSerializer

# Create your views here.


# Users Viewset
class UserViewsets(viewsets.ModelViewSet):
    """
    User Viewsets
    - Create
    - Login ,Logout
    """

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs) -> Response:
        return utils.registerUser(self, request, models)

    def update(self, request, *args, **kwargs) -> Response:
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs) -> Response:
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request) -> Response:
        return utils.userLogin(request)

    @action(detail=False, methods=["get"])
    def logout(self, request) -> Response:
        return utils.userLogout(request)


# Profile Viewsets
class ProfileViewsets(viewsets.ModelViewSet):
    """
    Profile Viewsets
    - List ,Update ,Delete
    """

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    lookup_field = "username"
    search_fields = ["username", "name"]

    def create(self, request, *args, **kwargs) -> Response:
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs) -> Response:
        return utils.upateProfile(self, request)

    def perform_destroy(self, instance):
        instance.user.delete()
        instance.delete()

    @action(
        detail=True,
        methods=["get"],
        serializer_class=PostSerializer,
        permission_classes=[IsOwnerOrReadOnly, IsAuthenticated],
        search_fields=None,
    )
    def posts(self, request, username=None):
        posts = Post.objects.filter(profile=self.get_object())
        return Response(self.get_serializer(posts, many=True).data)
