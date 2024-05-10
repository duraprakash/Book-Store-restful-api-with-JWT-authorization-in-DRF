from rest_framework import serializers
from .models import Author, Book, Category, SubCategory

# all fields serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    # # uncomment this to show details instead of id
    # authors = AuthorSerializer(many=True)
    # category = CategorySerializer()
    # sub_category = SubCategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'
        # lookup_field = ['slug','pk']
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug', 'lookup_field': 'pk'}
        # }