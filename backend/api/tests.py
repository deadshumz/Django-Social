from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testname", password="testpass")

    def test_profile_exist(self):
        test_user = User.objects.get(username="testname")
        self.assertEqual(test_user, test_user.profile.user)
