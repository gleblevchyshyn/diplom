from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:page>/', views.book_list, name='book_list_paginated'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('', views.book_list, name='book_list'),
]
