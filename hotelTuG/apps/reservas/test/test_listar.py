from . import ReservasBaseTest, status, reverse


class ReservaListarTest(ReservasBaseTest):
    def test_listar_reservas(self):
        response = self.client.get(self.urls['listar'], headers=self.header_user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
