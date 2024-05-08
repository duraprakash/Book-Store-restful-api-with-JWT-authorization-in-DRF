from django.urls import path
from .views import (
    # Category
    CategoryListView,
    CategoryCreateView,
    CategoryRetrieveView,
    CategoryUpdateView,
    CategoryDeleteView,
    
    # Sub-Category
    SubCategoryListView,
    SubCategoryCreateView,
    SubCategoryRetrieveView,
    SubCategoryUpdateView,
    SubCategoryDeleteView,
    
    # Author
    AuthorListView,
    AuthorCreateView,
    AuthorRetrieveView,
    AuthorUpdateView,
    AuthorDeleteView,
    
    # Book
    BookListView,
    BookCreateView,
    BookRetrieveView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # path('', ),
    
    # Category
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/', CategoryRetrieveView.as_view(), name='category_retrieve'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    
    # Sub-Category
    path('subcategories/', SubCategoryListView.as_view(), name='subcategories'),
    path('subcategory/create/', SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory/<int:pk>/', SubCategoryRetrieveView.as_view(), name='subcategory_retrieve'),
    path('subcategory/<int:pk>/update/', SubCategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory/<int:pk>/delete/', SubCategoryDeleteView.as_view(), name='subcategory_delete'),
    
    # Author
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/', AuthorRetrieveView.as_view(), name='author_retrieve'),
    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    
    # Book
    path('', BookListView.as_view(), name='books'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/', BookRetrieveView.as_view(), name='book_retrieve'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
