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
    
    
class Coffee(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    coffee_pic = models.CharField(max_length=300)
    price = models.IntegerField()
    stock_quantity = models.IntegerField(null=True)
    discount_percentage = models.IntegerField(blank = True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def price_after_discount(self):
        price = int(self.price*((100-self.discount_percentage)/100))
        return price     
    
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    item = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return self.item.name


class InternalData(models.Model):
    shipping_fee = models.IntegerField()
    tax_percentage = models.IntegerField()
    
    def __str__(self):
        return "InternalData"


class Orders(models.Model):
    order_id = models.CharField(unique=True, max_length=300)
    coffees = models.JSONField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    after_tax_amount = models.FloatField()
    house_number = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    other_addresses = models.CharField(max_length=200)
    instructions = models.CharField(max_length=300)
    status_choices = {"DLV" : "Delivered",  
        "PND" : "Pending", 
        "OTW" : "On The Way", 
        "XXD" : "Cancelled"
        }
    status = models.CharField(max_length=200, choices=status_choices)
    total_items = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def before_tax(self):
        coffees = self.coffees
        order_total_before_tax = float(sum([coffee["total_price"] for coffee in coffees ]))
        return order_total_before_tax   
    
    
    
    def __str__(self):
        return f"{self.user.first_name}'s order number {self.id}" 
    
    
    

    
    
    
    