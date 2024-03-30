from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Profile
class Profile(models.Model):
    """
    User Profile
    - username ,password ,email ,joined on
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="media/profile-pictures/",
        null=True,
    )
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=50, null=True, blank=False)
    name = models.CharField(max_length=50, null=False, blank=True)
    bio = models.TextField(null=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
