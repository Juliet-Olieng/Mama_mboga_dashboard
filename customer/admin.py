from django.contrib import admin

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("name","email","contact","location","password","date_created")
admin.site.register(Customer,CustomerAdmin)


