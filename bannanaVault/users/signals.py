from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    """"""
    UserProfile.objects.create(user=instance)
    
