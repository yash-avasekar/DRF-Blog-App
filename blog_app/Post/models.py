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

    title = models.CharField(null=False, blank=False, max_length=50)
    content = models.CharField(null=True, blank=True, max_length=255)
    author = models.CharField(null=True, blank=True, max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    tag = models.CharField(null=True, blank=True, max_length=50)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile"
    )

    class Meta:
        ordering = ["-publication_date"]

    def __str__(self) -> str | None:
        return self.title


# Like
class Like(models.Model):
    """
    Like Model
    - like by profile ( user )
    - like on post
    """

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["profile", "post"]

    def __str__(self):
        return f"{self.profile} liked {self.post}"
