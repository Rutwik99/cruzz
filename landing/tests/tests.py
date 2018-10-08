import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from landing import views


class TestViewTest(TestCase):

    def test_test_view(self):
        self.assertEqual(views.test_func(), True)


class AuthAPITest(TestCase):

    def test_register_new_user(self):
        new_user = {
            "user":
            {
                "email": "mohit@yadav.com",
                "username": "peace",
                "password": "peacepeace",
                "is_staff": "True",
                "is_superuser": "True"
            }
        }
        view = views.RegistrationAPIView.as_view()
        factory = APIRequestFactory()
        request = factory.post('/api/users/registration/', json.dumps(new_user), content_type='application/json')
        response = view(request)
        response_email = response.data['email']
        response_username = response.data['username']
        response_code = response.status_code
        with self.subTest():
            self.assertEqual(response_email, 'mohit@yadav.com')
        with self.subTest():
            self.assertEqual(response_username, 'peace')
        with self.subTest():
            self.assertEqual(response_code, 201)
