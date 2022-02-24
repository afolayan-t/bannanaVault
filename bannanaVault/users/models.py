from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
###### TODO: Create Base User Model
class UserProfile(User):
    """User account profile, contains information pertaining to a particular user"""
    # profile_picture
    profile_pic = models.ImageField() # profile pictures will be from a predetermined pool of photos
    



