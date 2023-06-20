from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Bookhasgenres)
admin.site.register(Language)
admin.site.register(Discount)
admin.site.register(Genre)
admin.site.register(Format)
admin.site.register(Bookhasauthor)
