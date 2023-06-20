from django.contrib import admin

# Register your models here.
from .models import Notifications
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ("recipient","message","date","type_of_notification","date_created")
admin.site.register(Notifications,NotificationsAdmin)

