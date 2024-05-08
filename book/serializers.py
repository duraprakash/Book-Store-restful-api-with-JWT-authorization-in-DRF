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
    class Meta:
        model = Book
        fields = '__all__'
        
# create override serializers
class CategoryCreateSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    athor = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = '__all__'
        
    # def create(self, validated_data):
    #     name= validated_data.get('name',None)
    #     user=Category.objects.create(
    #         name=name,
    #     )
    #     return user


class SubCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'