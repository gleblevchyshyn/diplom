from django.urls import path
from . import views

urlpatterns = [
    path('top_books/', views.top_books, name='top_books'),
    path('search/', views.search, name='search'),
    path('personal_recs/', views.personal_recs, name='personal_recs'),
]
