from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Profile
class Profile(models.Model):
    """
    User Profile
    - username ,password ,email ,joined on
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
