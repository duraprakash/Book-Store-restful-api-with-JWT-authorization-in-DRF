from django.urls import path
from .views import (# Author
    AuthorListView, # Book
    BookListView,
    # Category
    CategoryListView, # Sub-Category
    SubCategoryListView, AuthorCreateView,
    AuthorDeleteView, AuthorRetrieveView, AuthorUpdateView, BookCreateView, BookDeleteView,
    BookRetrieveSlugView, BookRetrieveView, BookSimilarRetrieveSlugView, BookUpdateView,
    CategoryCreateView, CategoryDeleteView, CategoryRetrieveView, CategoryUpdateView,
    CommentCreateView, CommentDeleteView, CommentDetailsView, CommentUpdateView, CommentView,
    SubCategoryCreateView, SubCategoryDeleteView, SubCategoryRetrieveView, SubCategoryUpdateView)

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
    
    path('<slug:slug>/slug-kwargs/', BookRetrieveSlugView.as_view(), name='book_retrieve_slug_path'), # slug from path ie: http://127.0.0.1:8000/books/fantastic-four1/slug-kwargs/
    path('slug-params/', BookRetrieveSlugView.as_view(), name='book_retrieve_slug_params'), # slug from params ie: http://127.0.0.1:8000/books/slug-params/?slug=fantastic-four1
    
    path('<slug:slug>/slug-kwargs/similar/', BookSimilarRetrieveSlugView.as_view(), name='book_retrieve_slug_similar_path'), # slug from path ie: http://127.0.0.1:8000/books/fantastic-four/slug-kwargs/similar/
    path('slug-params/similar/', BookSimilarRetrieveSlugView.as_view(), name='book_retrieve_slug_similar_params'), # slug from params ie: http://127.0.0.1:8000/books/slug-params/similar/?slug=fantastic-four
    
    path('comments/', CommentView.as_view(), name='comment-list'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', CommentDetailsView.as_view(), name='comment-retrieve'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
