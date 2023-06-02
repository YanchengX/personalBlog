from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Signup

class SignupTest(APITestCase):
    def setUp(self):
        #test data
        Signup.objects.create(account= 'baoc', pwd='123')
        Signup.objects.create(account= 'yan', pwd='169')

    def test_get_all_signup(self):
        # Send a GET request to the API endpoint
        url = reverse('newapp:signup')  # Assuming you have a 'signup' URL pattern
        response = self.client.get(url)

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the response data
        account = response.data
        self.assertEqual(len(account), 3)  # Assuming we created 3 posts in the setup method

        # Verify the content of the first post
        first_post = account[0]
        self.assertEqual(first_post['account'], 'baoc')
        self.assertEqual(first_post['pwd'], '123')

