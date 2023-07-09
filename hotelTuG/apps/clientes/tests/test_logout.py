from . import TestBase


class TestLogout(TestBase):
    def test_valid_logout(self):
        response = self.client.post(self.urls.get("logout"), data={
                                    "refresh_token": self.refresh_token}, format='json')
        self.assertEqual(response.status_code, 205)
        self.assertTrue(response.data['success'])

    def test_invalid_logout(self):
        response = self.client.post(self.urls.get("logout"), {}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.data['success'])
# coverage run --source='.' manage.py test apps