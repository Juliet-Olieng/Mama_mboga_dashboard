from django.contrib import admin

# Register your models here.
from .models import Rating
class RatingAdmin(admin.ModelAdmin):
    list_display = ("sender","value","date","product","review_message","date_created")
admin.site.register(Rating,RatingAdmin)
