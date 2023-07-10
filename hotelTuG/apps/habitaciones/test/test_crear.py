from . import HabitacionesBaseTest
from rest_framework import status, reverse


class HabitacionesCrearTest(HabitacionesBaseTest):
    def test_crear_habitacion(self):
        url = self.urls['crear']
        data = {
            'numero': 3,
            'piso': 4,
            'precio': 200.00,
            'estado': False,
            'descripcion': 'Nueva habitación',
            'tipo': 'M'
        }
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token_super_user)
        response = self.client.post(url, data,  headers=self.header_super_user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['numero'], '3')
