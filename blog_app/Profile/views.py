from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.contrib.auth import logout

from . import models
from . import serializers
from . import utils

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

    def update(self, request, *args, **kwargs):
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request) -> Response:
        return utils.userLogin(request)

    @action(detail=False, methods=["get"])
    def logout(self, request) -> Response:
        logout(request)
        return Response(status=status.HTTP_200_OK)


# User Login


# Profile Viewsets
class ProfileViewsets(viewsets.ModelViewSet):
    """
    Profile Viewsets
    - List ,Update ,Delete
    """

    serializer_class = serializers.ProfileSerializer

    def get_queryset(self):
        return models.Profile.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs) -> Response:
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return utils.upateProfile(self, request)

    def perform_destroy(self, instance):
        instance.user.delete()
        instance.delete()
