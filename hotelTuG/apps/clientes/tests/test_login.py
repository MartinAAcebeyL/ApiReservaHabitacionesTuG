from . import TestBase


class TestLogin(TestBase):
    def test_valid_login(self):
        response = self.client.post(self.urls.get("login"), {
            "email": self.user.email,
            "password": "123456"
        })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['success'])
        self.assertIn('token', response.data['data'])
        self.assertIn('refresh-token', response.data['data'])

    def test_invalid_email_format(self):

        response = self.client.post(self.urls.get("login"), {
            "email": self.user.email,
            "password": "test"
        })

        self.assertEqual(response.status_code, 401)
        self.assertFalse(response.data['success'])
        self.assertEqual(response.data['message'],
                         'Email or password incorrect')

