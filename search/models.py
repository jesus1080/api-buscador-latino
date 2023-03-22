from django.db import models

# Create your models here.

class Search(models.Model):
    palabra = models.CharField(max_length=200)
    resumen = models.TextField
    contenido = models.TextField
    