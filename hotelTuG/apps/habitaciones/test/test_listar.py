from . import HabitacionesBaseTest
from rest_framework import status, reverse


class HabitacionesListarTest(HabitacionesBaseTest):
    def test_listar_habitaciones(self):
        url = self.urls['listar']
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
