from django.test import TestCase
from .models import CustomUser
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    def setUp(self):
        self.data = {'username': 'testname', 'password': 'testpass'}
        self.user = CustomUser.objects.create_user(
            username=self.data['username'], password=self.data['password'])
        response = self.client.post('/api/token/', data=self.data)
        self.access_token = response.data['access']

    def test_get_self_endpoint(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get('/api/users/self/')
        self.assertEqual(response.data['username'], self.user.username)

    def test_self_get_access(self):
        response = self.client.get('/api/users/self/')
        self.assertEqual(404, response.status_code)
