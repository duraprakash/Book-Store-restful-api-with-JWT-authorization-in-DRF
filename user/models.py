from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    
class User(AbstractUser):
    # first_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)
    seller = models.BooleanField(default=False)
    # buyer = models.BooleanField(default=False) # only one needed
    address = models.ForeignKey(Address, verbose_name=_("User Address"), on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.username
    