from django.db import models

# Create your models here.
# 
class Notification(models.Model):
      recipient =models.CharField(max_length=32)
      message = models.TextField(max_length=100)
      date = models.DateField()
      type_of_notification = models.CharField(max_length=32)
      date_created = models.DateTimeField(auto_now_add=True)
      date_update = models.DateTimeField(auto_now=True)
      def __str__(self):
          return self.recipient
