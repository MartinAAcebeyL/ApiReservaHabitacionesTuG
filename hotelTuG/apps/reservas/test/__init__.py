from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.habitaciones.models import Habitacion
from apps.clientes.models import Cliente
from apps.users.models import User
from apps.reservas.models import Reserva
from datetime import datetime, timedelta


class ReservasBaseTest(APITestCase):
    def setUp(self):
        self.urls = {
            'listar': reverse('reserva-listar'),
            'crear': reverse('reserva-crear'),
            "login": reverse("login"),
        }

        self.habitacion = Habitacion.objects.create(
            numero=101,
            piso=1,
            precio=100.0,
            estado=False,
            descripcion="Habitación individual",
            tipo="S",
        )

        self.habitacion_ocupada = Habitacion.objects.create(
            numero=51,
            piso=1,
            precio=100.0,
            estado=True,
            descripcion="Habitación individual",
            tipo="S",
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

        self.reserva = Reserva.objects.create(
            cliente=self.user,
            habitacion=self.habitacion,
            fecha_inicio="2022-01-01",
            fecha_fin="2022-01-10",
            monto=1,
            metodo_pago="E",
            estado="P",
        )
        return super().setUp()
