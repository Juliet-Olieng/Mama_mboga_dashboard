from django.contrib import admin

# Register your models here.
from .models import Notification
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("recipient","message","date","type_of_notification","date_created")
admin.site.register(Notification,NotificationAdmin)

