from django.db import models

# Create your models here.


class Clientes(models.Model):
    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['apellido']
        
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)
