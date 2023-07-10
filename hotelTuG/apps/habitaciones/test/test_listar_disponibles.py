from rest_framework import status
from django.urls import reverse
from apps.habitaciones.models import Habitacion
from rest_framework.test import APITestCase


class HabitacionesListarDisponiblesTest(APITestCase):
    def setUp(self):
        Habitacion.objects.create(
            numero=1, piso=1, precio=100, estado=True, descripcion='Habitación 1', tipo='S')
        Habitacion.objects.create(
            numero=2, piso=1, precio=150, estado=False, descripcion='Habitación 2', tipo='D')
        Habitacion.objects.create(
            numero=3, piso=2, precio=200, estado=False, descripcion='Habitación 3', tipo='M')
        Habitacion.objects.create(
            numero=4, piso=2, precio=250, estado=True, descripcion='Habitación 4', tipo='S')

    def test_listar_habitaciones_disponibles(self):
        url = reverse('listar-habitaciones-disponibles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        response = self.client.get(
            url, {'precio_max': 200, 'tipo[]': ['S', 'D']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        response = self.client.get(url, {'precio_max': 100, 'tipo[]': ['M']})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
