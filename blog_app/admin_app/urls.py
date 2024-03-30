from rest_framework.routers import DefaultRouter

from . import views

# Admin urls

router = DefaultRouter()
router.register("profiles", views.ProfilesViewsets)
router.register("posts", views.PostsViewsets)
router.register("likes", views.LikeViewsets)
router.register("comments", views.CommentsViewsets)


urlpatterns = router.urls
