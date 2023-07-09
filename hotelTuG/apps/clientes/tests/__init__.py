from django.urls import reverse
from rest_framework.test import APITestCase
from apps.clientes.models import Cliente


class TestBase(APITestCase):
    def setUp(self) -> None:
        self.urls = {
            "logout": reverse('logout'),
            "login": reverse("login"),
            "cliente_listar_crear": reverse("cliente_listar_crear"),
        }

        self.user = Cliente.objects.create_user(
            nombre="user",
            apellido="user",
            ci=111111,
            email="user@gmail.com",
            password="123456",
            fecha_nacimiento="1999-01-01",
        )
        self.user.save()
        request = self.client.post(
            path=self.urls.get("login"),
            data={
                "email": self.user.email,
                "password": "123456"
            },
            format='json'
        )

        self.token = request.data['data']['token']
        self.refresh_token = request.data['data']['refresh-token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()