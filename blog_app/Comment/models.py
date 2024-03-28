from django.db import models
from Post.models import Post
from Profile.models import Profile

# Create your models here.


# Comment
class Comment(models.Model):
    """
    Comment
    - comment on post, comment by profile( user )
    - comment text, commented_on
    """

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-commented_on"]

    def __str__(self) -> str:
        return self.comment_text
