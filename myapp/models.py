from django.db import models

# Create your models here.
class Trabajos(models.Model):
    descripcion = models.CharField(max_length=50)
    lugar = models.CharField(max_length=20)


