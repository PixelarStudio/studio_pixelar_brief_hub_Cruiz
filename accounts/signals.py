# accounts/signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance: User, created: bool, **kwargs):
    """
    Garantiza que TODO usuario tenga Profile.
    - Si no existe, lo crea (tanto al crear el usuario como en cualquier save,
      por ejemplo en el login cuando actualiza last_login).
    - No intenta acceder a instance.profile directamente para evitar RelatedObjectDoesNotExist.
    """
    Profile.objects.get_or_create(user=instance)
