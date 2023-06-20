from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("name","amount","status","date","method_of_payment","date_created")
admin.site.register(Payment,PaymentAdmin)
