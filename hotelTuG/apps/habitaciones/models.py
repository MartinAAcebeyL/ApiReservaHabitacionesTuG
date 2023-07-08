from django.db import models


class Habitaciones(models.Model):
    class Meta:
        db_table = 'habitaciones'
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
        ordering = ['piso', 'numero']

    TIPO_CHOICES = (
        ('S', 'Simple'),
        ('D', 'Doble'),
        ('M', 'Matrimonial'),
        ('Su', 'Suite')
    )

    numero = models.DecimalField(max_digits=4, decimal_places=0)
    piso = models.DecimalField(max_digits=2, decimal_places=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
