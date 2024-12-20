from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.titulo  # Devolver solo el título como cadena