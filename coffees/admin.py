from django.contrib import admin
from coffees.models import Category, coffee, cart

# Register your models here.
admin.site.register([Category, coffee, cart])    