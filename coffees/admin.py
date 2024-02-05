from django.contrib import admin
from coffees.models import Category, Coffee, Cart, InternalData, Orders

# Register your models here.
admin.site.register([Category,Cart, InternalData, Orders])

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['category', "name", "price"]
    list_filter = ['category']
    sortable_by = ["name", "price"]