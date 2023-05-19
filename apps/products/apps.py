from django.apps import AppConfig
from django.core.cache import cache
from django.core.paginator import Paginator


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'