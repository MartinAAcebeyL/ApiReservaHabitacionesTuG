from django.db import models
from apps.users.models import Users

class Cliente(Users):
    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
