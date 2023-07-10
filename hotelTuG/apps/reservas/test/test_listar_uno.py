from . import ReservasBaseTest, status, reverse


class ReservaListarUnoTest(ReservasBaseTest):
    def test_listar_una_reserva(self):
        url = reverse("reserva-listar-uno", args=[self.reserva.pk])
        response = self.client.get(url, headers=self.header_user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
