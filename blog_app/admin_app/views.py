from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from Profile.models import Profile
from Post.models import Post, Like
from Comment.models import Comment
from Profile.serializers import ProfileSerializer, UserSerializer
from Post.serializers import LikeSerializer, PostSerializer
from Comment.serializers import CommentSerializer


# Create your views here.

# Admin Viewsets


# Profiles
class ProfilesViewsets(ModelViewSet):
    """
    Admin Viewsets to view all Profiles
    - CRUD
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "username"


# Posts
class PostsViewsets(ModelViewSet):
    """
    Admin Viewsets to view all Posts
    - CRUD
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]


# Likes
class LikeViewsets(ModelViewSet):
    """
    Admin Viewsets to view all Likes
    - CRUD
    """

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAdminUser]


# Comments
class CommentsViewsets(ModelViewSet):
    """
    Admin Viewsets to view all Comments
    - CRUD
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]
