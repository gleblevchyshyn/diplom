# from django.contrib.auth.models import User
# from django.test import TestCase
# from django.urls import reverse
# from django.apps import apps
#
#
# class RecommendationViewsTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client.login(username='testuser', password='testpassword')
#         self.rec_sys = apps.get_app_config('recommendations').recommendation_system
#
#     def test_top_books_view(self):
#         response = self.client.get(reverse('top_books'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'book_list.html')
#
#     def test_search_view(self):
#         query = 'fantasy'
#         response = self.client.post(reverse('search'), {'query': query})
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'book_list.html')
#
#     def test_personal_recs_view(self):
#         response = self.client.get(reverse('personal_recs'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'book_list.html')
#
#     def test_personal_recs_view_with_predictions(self):
#         # Mock the predict method to return a list of book IDs
#         self.rec_sys.predict = lambda user_id: [1, 2, 3, 4, 5]
#
#         response = self.client.get(reverse('personal_recs'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'book_list.html')
#         # Check if the returned books match the mocked predictions
#         books = response.context['books']
#         self.assertEqual(len(books), 5)
#         self.assertEqual([book.idbook for book in books], [1, 2, 3, 4, 5])
#
#         # Clean up the mock
#         del self.rec_sys.predict
