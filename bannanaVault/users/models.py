from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
###### TODO: Create Base User Model
class UserProfile(models.Model):
    """User account profile, contains information pertaining to a particular user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserProfile')
    # profile_picture
    profile_pic = models.CharField(max_length=11, null=True) # profile pictures will be from a predetermined pool of photos

    



