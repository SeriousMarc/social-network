from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.profile_data = {'bio': 'Go f yourself'}
        self.response = self.client.post(
            reverse('create'),
            self.profile_data,
            format="json")

    def test_can_create_profile(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
