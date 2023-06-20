from django.urls import path
from . import views

urlpatterns = [
    path('previous_orders/', views.previous_orders, name='previous_orders'),
    path('cart/', views.cart, name='cart'),
    path('cart/add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),
    path('update_quantity/<int:book_id>/', views.update_quantity, name='update_quantity'),
    path('make_order/', views.make_order, name='make_order'),
    path('admin_orders/', views.admin_orders, name='admin_orders')
]