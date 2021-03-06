import random 
from string import ascii_letters
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User
from passwords.password_generator import generate_password_advanced


# Create your models here.
punctuation = r"""!"#$%&'()*+,-./:;=?@[]^_`{|}~"""

# class StandardSites(models.TextChoices):
#     ntfx = 'netflix'
#     twtr = 'twitter'
#     fb = 'facebook'
#     rdt = 'reddit'
#     yt = 'youtube'
#     gg = 'google'

# class PasswordRules(models.TextChoices):
#     """These are rules for passwords to follow"""
#     # at least 8 chars
#     # a mixture of both uppercase and lowercase letters
#     # a mixture of numbers and letters
#     # include at least on special char sans < or >


class PasswordVault(models.Model):
    """The model that maintains connections between users and password entries, as well as any other things that exist for that user outside of there profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='password_vault')
    note = models.TextField() # note pad feature

class PasswordEntry(models.Model):
    """Password Entries where passwords are stored and modified."""
    site_name = models.CharField(max_length=50)
    site_url = models.CharField(max_length=60, null=True)
    auth_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True)
    # email or username
    vault = models.ForeignKey(PasswordVault, on_delete=models.CASCADE, related_name='password_entry', null=True)

    # TODO: et puis, hash password, figure out how to hash this password
    def hash_password(self, password, commit=True):
        """before storing password, hash with this function."""
        hashed_password = make_password(password, salt=self.site_name)
        self.password = hashed_password
        print(f'in hash_password(): {self.password}')
        self.save(commit)
