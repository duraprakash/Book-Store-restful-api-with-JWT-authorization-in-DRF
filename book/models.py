from django.db import models
from user.models import User
from django.template.defaultfilters import slugify

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
    
    class Meta:
        unique_together = ['name', 'dob']
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='media')
    isnb = models.CharField(max_length=50)
    category = models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, verbose_name=("Sub Category"), on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, verbose_name=("Authors"))
    price = models.FloatField(default=0)
    stock_quantity = models.PositiveIntegerField(default=0)
    publication = models.CharField(max_length=50)
    publication_date = models.DateField()
    slug = models.SlugField(default=None, null=False, unique=True)
    is_available = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, verbose_name=("Added By"), on_delete=models.CASCADE) # book adding by same user issuse fixed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.slug

    
    
    