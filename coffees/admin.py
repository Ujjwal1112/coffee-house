from django.contrib import admin
from coffees.models import Category, Coffee, Cart, InternalData

# Register your models here.
admin.site.register([Category, Coffee, Cart, InternalData])    