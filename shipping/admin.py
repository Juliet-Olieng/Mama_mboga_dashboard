from django.contrib import admin
from .models import Shipping

# Register your models here.
class ShippingAdmin(admin.ModelAdmin):
    list_display = ("shippingServive","shippingLocation","ShippingMethod","handlingTime","date_created","transitTime")
    
admin.site.register(Shipping,ShippingAdmin)
