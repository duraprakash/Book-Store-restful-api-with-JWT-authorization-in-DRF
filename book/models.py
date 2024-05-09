from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    name = models.CharField(max_length=50)
    dob = models.DateField(null=True,blank=True)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='media')
    isnb = models.CharField(max_length=50)
    category = models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, verbose_name=("Sub Category"), on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, verbose_name=("Author"))
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publication = models.CharField(max_length=50)
    publication_date = models.DateField()
    slug = models.SlugField(default="", null=False)
    is_available = models.BooleanField(default=False)
    added_by = models.OneToOneField(User, verbose_name=("Added By"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.slug

    
    
    