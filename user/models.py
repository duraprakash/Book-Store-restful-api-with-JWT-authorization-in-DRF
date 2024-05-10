from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Geo(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    # geo = models.ForeignKey(Geo, verbose_name=_("Geo"), on_delete=models.SET_NULL, null=True)
    
class User(AbstractUser):
    updated_at = models.DateTimeField(auto_now_add=True)
    seller = models.BooleanField(default=False)
    address = models.ForeignKey(Address, verbose_name=_("User Address"), on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.username
    