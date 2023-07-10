from . import ReservasBaseTest, status, reverse


class ReservaActualizarTest(ReservasBaseTest):
    def test_actualizar(self):
        data = {"monto": 50,
                "estado": "Pa",
                "metodo_pago": "E",
                "habitacion": self.habitacion.id
                }
        response = self.client.put(
            reverse('reserva-actualizar', args=[self.reserva.id]), data, format="json", headers=self.header_super_user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_actualizar_reserva_sin_autenticacion(self):
        data = {"monto": 50,
                "estado": "Pa",
                "metodo_pago": "E",
                "habitacion": self.habitacion.id
                }
        response = self.client.put(
            reverse('reserva-actualizar', args=[self.reserva.id]), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
