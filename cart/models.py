from django.db import models
from inventory2.models import Product
from Order.models import Order

# Create your models here.
class Cart(models.Model):
    order1=models.ForeignKey(Order, on_delete=models.CASCADE)
    products=models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.PositiveIntegerField()
    shippingCost=models.DecimalField(max_digits=6,decimal_places=2)
    paymentOptions = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    def __str__(self):
          return self.paymentOptions