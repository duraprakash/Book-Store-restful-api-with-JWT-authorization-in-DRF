from rest_framework import serializers
from .models import Author, Book, Category, Comment, SubCategory

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
        
class CommentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Comment
        fields = '__all__'
        
    # def create(self, validated_data):
    #     validated_data['is_visible'] = True
    #     return super().create(validated_data)
        
class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = '__all__'

class BookCommentSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['id', 'title', 'image', 'isnb', 'category', 'sub_category', 'authors', 'price', 'stock_quantity', 'publication', 'publication_date', 'slug', 'is_available', 'added_by', 'comments', 'created_at', 'updated_at']
    def get_comments(self, obj):
        comments = Comment.objects.filter(book=obj, is_visible=False)
        return CommentSerializer(comments, many=True).data
    
class BookSlugSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    category = CategorySerializer()
    sub_category = SubCategorySerializer()

    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['title', 'category', 'authonrs', 'category', 'sub_category']
        
# class BookSlugSerializer(serializers.ModelSerializer):
#     # authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
#     # uncomment this to show details instead of id
#     authors = AuthorSerializer(many=True)
#     category = CategorySerializer()
#     sub_category = SubCategorySerializer()

#     class Meta:
#         model = Book
#         fields = '__all__'
        
#         # lookup_field = ['slug','pk']
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug', 'lookup_field': 'pk'}
#         # }


