from django.db import models
from Order.models import Order

# Create your models here.
class Shipping(models.Model):
    order=models.ManyToManyField(Order)
    shippingServive= models.DateField(auto_created=True)
    shippingLocation=models.CharField(max_length=32)
    ShippingMethod = models.CharField(max_length=32)
    handlingTime = models.DurationField()
    transitTime = models.DurationField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
          return self.ShippingMethod
