from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid
from django.contrib.auth.hashers import make_password, check_password
from .managers import CustomUserManager


class Users(AbstractBaseUser):
    objects = CustomUserManager()
    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    username = None

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Users, self).save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
