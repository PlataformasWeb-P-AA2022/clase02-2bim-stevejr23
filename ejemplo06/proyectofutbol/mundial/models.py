from django.db import models

# Create your models here.

class Estadio(models.Model):
    nombre = models.CharField(max_length=30)
    capacidad = models.IntegerField()


    def __str__(self):
        return "%s - capacidad: %d" % (self.nombre,
                self.capacidad)

class Equipo(models.Model):
    """
    """
    siglas = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    sobrenombre = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s - %s " % (self.siglas,
        self.nombre,self.sobrenombre)


