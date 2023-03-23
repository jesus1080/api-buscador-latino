from django.db import models
from django.utils import timezone

# Create your models here.

class Search(models.Model):
    palabra = models.CharField(max_length=200)
    resumen = models.TextField(default='')
    contenido = models.TextField(default='')
    create_at = models.DateTimeField(default=timezone.now)
    