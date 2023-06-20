from django.db import models

# Create your models here.
class Rating(models.Model):
      sender =models.CharField(max_length=32)
      review_message = models.TextField(max_length=100)
      date = models.DateField()
      value = models.PositiveIntegerField()
      product = models.CharField(max_length=32)
      date_created = models.DateTimeField(auto_now_add=True)
      date_update = models.DateTimeField(auto_now=True)
      def __str__(self):
          return self.sender
