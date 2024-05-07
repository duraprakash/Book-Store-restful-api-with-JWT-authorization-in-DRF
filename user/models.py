from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # first_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)
    seller = models.BooleanField(default=False)
    # buyer = models.BooleanField(default=False) # only one needed
    
    def __str__(self):
        return self.username