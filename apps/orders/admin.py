from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(Orderstatus)
admin.site.register(Deliverycompany)
admin.site.register(Branch)
admin.site.register(Payment)
