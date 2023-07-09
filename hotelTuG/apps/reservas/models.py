from django.db import models


class Reserva(models.Model):
    class Meta:
        db_table = 'reservas'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-fecha_inicio']

    ESTADO_CHOICES = (
        ('Pa', 'Pagado'),
        ('P', 'Pendiente'),
        ('E', 'Eliminado')
    )

    METODO_PAGO_CHOICES = (
        ('E', 'Efectivo'),
        ('T', 'Tarjeta'),
        ('Tr', 'Transferencia')
    )

    habitacion = models.ForeignKey(
        'habitaciones.Habitacion', on_delete=models.CASCADE)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=2, choices=METODO_PAGO_CHOICES)
