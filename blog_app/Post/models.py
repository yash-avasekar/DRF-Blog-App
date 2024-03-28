from django.db import models
from Profile.models import Profile

# Create your models here.


# Post
class Post(models.Model):
    """
    Post Model
    - post by profile( user )
    - title, content, author, publication date, modification date, and tags.

    -- note update content
    """

    title = models.CharField(null=True, blank=True, max_length=50)
    content = models.CharField(null=False, blank=False, max_length=255)
    author = models.CharField(null=False, blank=False, max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    tag = models.CharField(null=True, blank=True, max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str | None:
        return self.title
