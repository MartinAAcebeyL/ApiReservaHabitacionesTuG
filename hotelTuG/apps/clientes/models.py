from apps.users.models import User

class Cliente(User):
    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
