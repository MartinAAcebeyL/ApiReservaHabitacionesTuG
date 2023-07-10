from . import HabitacionesBaseTest
from rest_framework import status
from django.urls import reverse


class HabitacionesListarUnoTest(HabitacionesBaseTest):
    def test_listar_una_habitacion(self):
        url = reverse('listar-una-habitaciones',
                      kwargs={'pk': self.habitacion.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['numero'], '1')
