from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.apps import apps
from django.test import Client

from ..users.models import NewUser


class RecommendationViewsTest(TestCase):
    def setUp(self):
        user = NewUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password="?xn5C#?;Q'b^{~7D",
            age=25,
            sex='M',
            phone='1234567890',
            cashback=100.00,
        )
        self.rec_sys = apps.get_app_config('recommendations').recommendation_system
        self.c = Client()

    def test_top_books_view(self):
        response = self.client.get(reverse('top_books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')

    def test_search_view(self):
        query = 'Space travelling'
        response = self.client.post(reverse('search'), {'query': query})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')

    def test_personal_recs_authenticated(self):
        # Authenticate the user
        user = NewUser.objects.get(email='testuser@example.com')
        authenticated = self.client.login(email=user.email, password="?xn5C#?;Q'b^{~7D")
        self.assertTrue(authenticated, f"Failed to authenticate user {user.email}")

        # Perform authenticated request
        response = self.client.get(reverse('personal_recs'))
        self.assertEqual(response.status_code, 200)

        # Additional assertions to help diagnose the issue
        self.assertContains(response, "Expected content in the response")
        # Add more assertions to validate the response

        # Optional: Print response content for further investigation
        print(response.content)


