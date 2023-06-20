from django.db import models

# Create your models here.
class Cart(models.Model):
      price = models.DecimalField(max_digits=6,decimal_places=2)
      quantity = models.PositiveIntegerField()
      shippingCost=models.DecimalField(max_digits=6,decimal_places=2)
      paymentOptions = models.CharField(max_length=32)
      date_created = models.DateTimeField(auto_now_add=True)
      date_update = models.DateTimeField(auto_now=True)
      def __str__(self):
          return self.paymentOptions