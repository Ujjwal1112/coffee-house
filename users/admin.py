from django.contrib import admin
from users.models import Profile, ConsumedCoffee
# Register your models here.
admin.site.register([Profile, ConsumedCoffee])
