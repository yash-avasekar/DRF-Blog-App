from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login


def registerUser(self, request, models):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
        user = models.User.objects.create_user(
            username=request.data.get("username"),
            password=request.data.get("password"),
        )

        profile = models.Profile.objects.create(
            user=user,
            username=user.username,
        )

        if profile:
            user.save()
            return Response(
                "User Registered Successfully", status=status.HTTP_201_CREATED
            )
        return Response(profile, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def userLogin(request):
    user = authenticate(
        request, username=request.data.get("username"), password=request.data.get("password")  # type: ignore
    )

    if user:
        login(request, user)
        return Response(status=status.HTTP_200_OK)
    return Response("Invalide Username or Password", status=status.HTTP_400_BAD_REQUEST)


# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------


# Profile update along with user
def upateProfile(self, request):
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    user = instance.user
    user.username = instance.username
    user.email = instance.email
    user.name = instance.name
    user.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
