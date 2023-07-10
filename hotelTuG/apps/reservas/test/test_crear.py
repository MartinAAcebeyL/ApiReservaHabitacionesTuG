from . import ReservasBaseTest, status
from datetime import datetime, timedelta


class ReservaCrearTest(ReservasBaseTest):
    def test_crear_reserva_cliente(self):
        data = {
            "habitacion": self.habitacion.id,
            "fecha_inicio": "2025-01-01",
            "fecha_fin": "2025-01-05",
            "monto": self.habitacion.precio,
            "cliente": self.user.id,
            "metodo_pago": "E",
            "estado": "P"
        }
        response = self.client.post(
            self.urls.get('crear'), data, format="json", headers=self.header_user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_crear_reserva_cliente_fechas_erroneas(self):
        data = {
            "habitacion": self.habitacion.id,
            "fecha_inicio": "2025-01-01",
            "fecha_fin": "2024-01-05",
            "monto": 5,
            "cliente": self.user.id,
            "metodo_pago": "E",
            "estado": "P"
        }
        response = self.client.post(
            self.urls.get('crear'), data, format="json", headers=self.header_user)
        error = response.data['non_field_errors'][0]
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error,
                         'La fecha de fin debe ser posterior a la fecha de inicio.')

    def test_crear_reserva_cliente_sobrepago(self):
        data = {
            "habitacion": self.habitacion.id,
            "fecha_inicio": "2025-01-01",
            "fecha_fin": "2025-01-05",
            "monto": self.habitacion.precio+50,
            "cliente": self.user.id,
            "metodo_pago": "E",
            "estado": "P"
        }
        response = self.client.post(
            self.urls.get('crear'), data, format="json", headers=self.header_user)
        error = response.data['non_field_errors'][0].__str__()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error,
                         'El monto pagado no puede ser mayor al precio de la habitación.')

    def test_crear_reserva_habitacion_ocupada(self):
        data = {
            "habitacion": self.habitacion_ocupada.id,
            "fecha_inicio": "2025-01-01",
            "fecha_fin": "2025-01-05",
            "monto": 5,
            "cliente": self.user.id,
            "metodo_pago": "E",
            "estado": "P"
        }
        response = self.client.post(
            self.urls.get('crear'), data, format="json", headers=self.header_user)
        error = response.data['non_field_errors'][0].__str__()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error,
                         'La habitación no está disponible.')

    def test_crear_reserva_fechas_ocupadas(self):
        data = {
            "habitacion": self.habitacion.id,
            "fecha_inicio": "2022-01-01",
            "fecha_fin": "2022-01-10",
            "monto": 5,
            "cliente": self.user.id,
            "metodo_pago": "E",
            "estado": "P"
        }
        response = self.client.post(
            self.urls.get('crear'), data, format="json", headers=self.header_user)
        error = response.data['non_field_errors'][0].__str__()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error,
                         'Las fechas de reserva chocan con una reserva existente.')

    def test_crear_reserva_sin_autenticacion(self):
        data = {
            "habitacion": self.habitacion.id,
            "fecha_inicio": datetime.now().isoformat(),
            "fecha_fin": (datetime.now() + timedelta(days=2)).isoformat(),
            "monto": 5,
            "cliente": self.user.id,
            "metodo_pago": "E",
            "estado": "P"
        }
        response = self.client.post(
            self.urls.get('crear'), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
