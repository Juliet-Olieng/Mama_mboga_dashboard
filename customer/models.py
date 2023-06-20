from django.db import models

# Create your models here.
class Customer(models.Model):
      password = models.CharField(max_length=32)
      email = models.CharField(max_length=32)
      name =models.CharField(max_length=32)
      location = models.CharField(max_length=32)
      contact = models.PositiveIntegerField()      
      date_created = models.DateTimeField(auto_now_add=True)
      date_update = models.DateTimeField(auto_now=True)
      def __str__(self):
          return self.name

