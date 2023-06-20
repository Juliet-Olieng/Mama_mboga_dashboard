from django.db import models

# Create your models here.
class Order(models.Model):
      name =models.CharField(max_length=32)
      date = models.DateField()
      quantity = models.PositiveIntegerField()
      total = models.DecimalField(max_digits=6,decimal_places=2)
      date_created = models.DateTimeField(auto_now_add=True)
      date_update = models.DateTimeField(auto_now=True)
      def __str__(self):
          return self.name
