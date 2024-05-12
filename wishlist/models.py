from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User

# Create your models here.
class Wishlist(models.Model):
    user_id = models.ForeignKey(User, verbose_name=_("user_id"), on_delete=models.CASCADE)
    