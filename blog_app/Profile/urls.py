from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

# urls ( endpoints ) goes here

router = DefaultRouter()
router.register("profiles", views.ProfileViewsets, basename="profiles")
router.register("user", views.UserViewsets, basename="user")

urlpatterns = router.urls

urlpatterns += [
    # path("register/", views.RegisterUserView.as_view()),
]
