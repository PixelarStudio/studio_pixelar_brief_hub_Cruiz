from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Brief(models.Model):
    title = models.CharField("Título de la página", max_length=200)       # Char 1
    client_name = models.CharField("Cliente / marca", max_length=200)     # Char 2
    service_type = models.CharField(
        "Tipo de servicio",
        max_length=100,
        help_text="Ej: Landing, Web completa, E-commerce, Branding"
    )
    body = RichTextField("Contenido / objetivos")                         # texto enriquecido
    reference_image = models.ImageField(
        "Imagen de referencia",
        upload_to="briefs/"
    )                                                                     # imagen
    created_at = models.DateField("Fecha de creación", auto_now_add=True) # fecha
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="briefs",
        verbose_name="Responsable"
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.client_name}"
