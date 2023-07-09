from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid
from django.contrib.auth.hashers import make_password, check_password
from .managers import CustomUserManager


class User(AbstractBaseUser):
    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    username = None

    id = models.CharField(primary_key=True, max_length=36,
                          default=uuid.uuid4, editable=False)

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.IntegerField()
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    password = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def set_password(self, password):
        self.password = make_password(password)
        self.save()

    def check_password(self, password):
        return check_password(password, self.password)
