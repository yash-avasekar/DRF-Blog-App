from rest_framework import viewsets

from . import models
from . import serializers

# Create your views here.


# Post Viewsets
class PostViewset(viewsets.ModelViewSet):
    """
    Post Viewset
    - List ,Create ,Update ,Delete
    """

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)