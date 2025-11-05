from django.db import models
from django.contrib.auth.models import User

def avatar_upload_to(instance, filename):
    return f"avatars/user_{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=avatar_upload_to, blank=True, null=True)
    bio = models.TextField("Biografía", blank=True)
    website = models.URLField("Sitio web", blank=True)
    birth_date = models.DateField("Fecha de nacimiento", blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
