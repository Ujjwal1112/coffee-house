from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    
    def __str__(self):
        return self.name
    
    
class coffee(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    coffee_pic = models.CharField(max_length=300)
    price = models.IntegerField()
    stock_quantity = models.IntegerField(null=True)
    discount_percentage = models.IntegerField(blank = True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name
    

class cart(models.Model):
    item = models.ForeignKey(coffee, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.item.name
    
    
    
    
    