from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StandardSites(models.TextChoices):
    ntfx = 'netflix'
    twtr = 'twitter'
    fb = 'facebook'
    rdt = 'reddit'
    yt = 'youtube'
    gg = 'google'

class PasswordVault(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='PasswordVault')

class PasswordEntry(models.Model):
    site_name = models.CharField(max_length=50)
    site_url = models.CharField(max_length=60)
    password = models.CharField(max_length=50)
    username= models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    user = models.ForeignKey(PasswordVault, on_delete=models.CASCADE, related_name='password_entries')

    # TODO: create a password generator
    # TODO: et puis, hash password, figure out how to hash this password