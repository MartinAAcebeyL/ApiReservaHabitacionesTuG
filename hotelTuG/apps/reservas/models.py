from django.db import models


class Reservas(models.Model):
    class Meta:
        db_table = 'reservas'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-fecha_inicio']

    ESTADO_CHOICES = (
        ('R', 'Reservado'),
        ('O', 'Ocupado'),
        ('C', 'Cancelado')
    )

    METODO_PAGO_CHOICES = (
        ('E', 'Efectivo'),
        ('T', 'Tarjeta'),
        ('Tr', 'Transferencia')
    )

    habitacion = models.ForeignKey(
        'habitaciones.Habitaciones', on_delete=models.CASCADE)
    cliente = models.ForeignKey('clientes.Clientes', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)
    fecha_registro = models.DateField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=2, choices=METODO_PAGO_CHOICES)
