from django.db import models
from django.contrib.auth.models import User
from coffees.models import Coffee
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_num = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    profile_url = models.CharField(max_length=400, blank=True, null=True) 
    
    def __str__(self):
        return self.user.first_name


class ConsumedCoffee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee = models.ForeignKey(Coffee, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} has consumed {self.coffee.name}"
    