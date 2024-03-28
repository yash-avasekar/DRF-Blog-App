from rest_framework.routers import DefaultRouter

from . import views

# url ( endpoints ) goes here

router = DefaultRouter()
router.register("", views.CommentViewsets)

urlpatterns = router.urls
