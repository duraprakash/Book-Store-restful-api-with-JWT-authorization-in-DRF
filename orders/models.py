from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _
from book.models import Book

# Create your models here.
class Order(models.Model):
    PENDING = "P"
    COMPLETED = "C"
    
    STATUS_CHOICES = ((PENDING, _("pending")), (COMPLETED, _("completed")))
    
    userId = models.ForeignKey(User, verbose_name=_("UserId"), on_delete=models.CASCADE) # this
    order_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING, blank=False, null=False)
    total_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Book ordered by- {self.userId}'
    
    
class OrderItem(models.Model):
    orderId = models.ForeignKey(Order, verbose_name=_("Order No."), on_delete=models.CASCADE)
    bookId = models.ForeignKey(Book, verbose_name=_("Book"), on_delete=models.CASCADE) # this
    order_quantity = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # class Meta:
    #     unique_together = ('orderId', 'bookId') # this
    
    def __str__(self):
        return f'Book- {self.bookId}'
    
    def cost(self):
        return round(self.order_quantity * self.bookId.price, 2) # TODO: 
    


    