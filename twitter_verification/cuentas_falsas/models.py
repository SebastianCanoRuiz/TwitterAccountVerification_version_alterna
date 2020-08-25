from django.db import models

# Create your models here.
class DatosComentarios(models.Model):
    id = models.IntegerField(primary_key=True)
    perfil = models.CharField(max_length=500)
    comentario = models.CharField(max_length=500)
    cantidad_palabras = models.PositiveIntegerField()
    comentarios_repetidos = models.DecimalField(max_digits=3, decimal_places=2)
    insultos = models.DecimalField(max_digits=3, decimal_places=2)
    emoticones = models.DecimalField(max_digits=3, decimal_places=2)
    multimedia = models.DecimalField(max_digits=3, decimal_places=2)
    links = models.DecimalField(max_digits=3, decimal_places=2)
    comentarios_raros = models.DecimalField(max_digits=3, decimal_places=2)
    label = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
      return self.video_title
