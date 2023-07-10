from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.habitaciones.models import Habitacion
from apps.clientes.models import Cliente
from apps.users.models import User


class HabitacionesBaseTest(APITestCase):
    def setUp(self):
        self.urls = {
            'listar': reverse('listar-habitaciones'),
            'crear': reverse('crear-habitaciones'),
            "login": reverse("login"),
        }
        self.habitacion = Habitacion.objects.create(
            numero=1,
            piso=2,
            precio=100.00,
            estado=False,
            descripcion='Habitación de prueba',
            tipo='S'
        )

        self.user = Cliente.objects.create_user(
            nombre="user",
            apellido="user",
            ci=111111,
            email="user@gmail.com",
            password="123456",
            fecha_nacimiento="1999-01-01",
        )
        self.user.save()

        request = self.client.post(
            path=self.urls.get("login"),
            data={
                "email": self.user.email,
                "password": "123456"
            },
            format='json'
        )

        self.token = request.data['data']['token']
        self.refresh_token = request.data['data']['refresh-token']
        self.header_user = {
            'Authorization': f'Bearer {self.token}'}

        self.super_user = User.objects.create_superuser(
            email="admin@gmail.com",
            password="123456",
        )
        self.super_user.save()

        request = self.client.post(
            path=self.urls.get("login"),
            data={
                "email": self.super_user.email,
                "password": "123456"
            },
            format='json'
        )

        self.token_super_user = request.data['data']['token']
        self.refresh_token_super_user = request.data['data']['refresh-token']
        self.header_super_user = {
            'Authorization': f'Bearer {self.token_super_user}'}

        return super().setUp()
