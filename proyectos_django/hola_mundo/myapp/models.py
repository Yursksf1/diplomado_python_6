from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.PositiveIntegerField(max_length=30)

    def __str__(self):
        return "{} - {}".format(self.nombre, self.valor)