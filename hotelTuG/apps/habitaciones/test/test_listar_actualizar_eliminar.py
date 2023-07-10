from . import HabitacionesBaseTest
from rest_framework import status
from apps.habitaciones.models import Habitacion
from django.urls import reverse


class HabitacionesListarActualizarEliminarTest(HabitacionesBaseTest):
    def test_actualizar_habitacion(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token_super_user)
        url = reverse('actualizar_eliminar_habitacion',
                      kwargs={'pk': self.habitacion.pk})
        data = {
            'numero': 2,
            'piso': 3,
            'precio': 150.00,
            'estado': True,
            'descripcion': 'Habitación actualizada',
            'tipo': 'D'
        }
        response = self.client.put(url, data, headers=self.header_super_user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['numero'], '2')

    def test_eliminar_habitacion(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token_super_user)
        url = reverse('actualizar_eliminar_habitacion',
                      kwargs={'pk': self.habitacion.pk})
        response = self.client.delete(url, headers=self.header_super_user)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habitacion.objects.filter(
            pk=self.habitacion.pk).exists())
