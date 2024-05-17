from django.contrib import admin
from .models import Author, Book, Category, Comment, SubCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Author)
admin.site.register(Comment)

class slug(admin.ModelAdmin):
    list_display = ("title", "added_by",)
    prepopulated_fields = {"slug": ("title", "added_by")}
admin.site.register(Book, slug)