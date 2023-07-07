from django.db import models
from vendor.models import Vendor

# Create your models here.
class Product(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.PositiveIntegerField()
    # timecramp
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name