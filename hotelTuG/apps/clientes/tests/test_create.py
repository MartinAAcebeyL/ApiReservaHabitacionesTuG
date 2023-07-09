from . import TestBase
from apps.clientes.models import Cliente


class TestCrearCliente(TestBase):
    def test_get_all_clients(self):
        response = self.client.get(self.urls.get("cliente_listar_crear"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), Cliente.objects.count())

    def test_create_new_client(self):
        data = {
            "nombre": "lucas",
            "apellido": "lucas",
            "ci": 2222,
            "email": "new@gmail.com",
            "password": 123456,
            "fecha_nacimiento": "2000-11-30"
        }
        response = self.client.post(self.urls.get(
            "cliente_listar_crear"), data=data)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Cliente.objects.count(), 2)


    def test_missing_required_fields(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(self.urls.get(
            "cliente_listar_crear"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Cliente.objects.count(), 1)

    def test_invalid_data(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'invalidemail',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.client.post(self.urls.get(
            "cliente_listar_crear"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Cliente.objects.count(), 1)

    
