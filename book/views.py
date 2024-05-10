from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Author, Book, Category, SubCategory
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer, SubCategorySerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

# Create your views here.
# Category
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryRetrieveView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    
class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    
class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Sub-Category
class SubCategoryListView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
class SubCategoryCreateView(CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
class SubCategoryRetrieveView(RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = 'pk'
    
class SubCategoryUpdateView(UpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = 'pk'
    
class SubCategoryDeleteView(DestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = 'pk' 
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Sub category deleted successfully"}, status=status.HTTP_204_NO_CONTENT) 

# Author
class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class AuthorCreateView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class AuthorRetrieveView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'
    
class AuthorUpdateView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'
    
class AuthorDeleteView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer   
    lookup_field = 'pk'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Author deleted successfully"}, status=status.HTTP_204_NO_CONTENT) 

# Book
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # # query params 1.1
    # # change in BookSerializer -> lookup_field, extra_kwargs
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     slug = self.request.query_params.get('slug', None)
    #     if slug is not None:
    #         queryset = queryset.filter(Q(slug__icontains=slug)) # SELECT * FROM book WHERE slug LIKE '%ref%';
    #     return queryset
    
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookRetrieveView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    # # query params
    # def get_object(self):
    #     queryset = self.get_queryset()

    #     # Try to retrieve by slug first
    #     slug = self.kwargs.get('slug')
    #     if slug is not None:
    #         # return queryset.filter(slug=slug).first()
    #         if slug == int(slug):
    #             return queryset.filter(Q(pk__icontains=slug))
    #         return queryset.filter(Q(slug__icontains=slug))
        
    #     # obj = queryset.first()
    #     # if obj is None:
    #     #     raise status.HTTP_404_NOT_FOUND
    #     # return obj
    #     # Fallback to the default b33
    
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    lookup_field = 'pk'  
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
