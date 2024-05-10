from django.contrib import admin
from .models import Address, Geo, User

# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Geo)