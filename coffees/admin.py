from django.contrib import admin
from coffees.models import Category, Coffee, Cart, InternalData, Orders

# Register your models here.
admin.site.register([Category, Coffee, Cart, InternalData, Orders])    