from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import UserProfile
from passwords.models import PasswordVault

@receiver(post_save, sender=User)
def create_user_profile(sender, created, instance, **kwargs):
    """"""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_password_vault(sender, created, instance, **kwargs):
    """"""
    if created:
        PasswordVault.objects.create(user=instance)

    

