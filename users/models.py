from django.db import models
from django.contrib.auth.models import User
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

