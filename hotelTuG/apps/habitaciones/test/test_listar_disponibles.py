from . import HabitacionesBaseTest
from rest_framework import status, reverse


class HabitacionesListarDisponiblesTest(HabitacionesBaseTest):
    def test_listar_habitaciones_disponibles(self):
        url = self.urls['disponibles']
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
