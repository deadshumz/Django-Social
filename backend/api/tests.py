from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class UserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testname", password="testpass")
        response = self.client.post(
            '/api/token/', data={'username': "testname", 'password': "testpass"})
        self.access_token = response.data['access']

    def test_profile_exist(self):
        test_user = User.objects.get(username="testname")
        self.assertEqual(test_user, test_user.profile.user)

    def test_get_self_endpoint(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.access_token)
        response = self.client.get('/api/users/self/')
        self.assertEqual(response.data['username'], self.user.username)

    def test_self_get_access(self):
        response = self.client.get('/api/users/self/')
        self.assertEqual('404', response.status_code)