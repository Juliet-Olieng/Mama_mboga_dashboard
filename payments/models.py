from django.db import models

# Create your models here.
class Payment(models.Model):
      amount = models.DecimalField(max_digits=6,decimal_places=2)
      order = models.CharField(max_length=32)
      name =models.CharField(max_length=32)
      status = models.CharField(max_length=32)
      method_of_payment = models.CharField(max_length=32)
      date = models.DateField()
      date_created = models.DateTimeField(auto_now_add=True)
      date_update = models.DateTimeField(auto_now=True)
      def __str__(self):
          return self.name
