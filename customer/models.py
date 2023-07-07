from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name =models.CharField(max_length=32)
    
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    user=models.OneToOneField(User,
                              on_delete=models.CASCADE,null=True)
    location = models.CharField(max_length=32)
    contact = models.PositiveIntegerField()      
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
          return self.name

