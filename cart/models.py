from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User
from book.models import Book
from django.utils.functional import cached_property

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Cart for {self.user.username}'
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_("Cart"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=_("Books"), on_delete=models.CASCADE)
    quantity = models.DecimalField(_("Quantity"), max_digits=5, decimal_places=2)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('cart', 'book')
        
    def __str__(self):
        return f'Cart Item- {self.cart}'

    @cached_property
    def cost(self):
        return round(float(self.quantity) * self.book.price, 2)