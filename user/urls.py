from django.urls import path
from .views import UserCreateView, Seller, UserListView, UserRetrieveView, UserUpdateView, UserDeleteView, LoginView, LogoutView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user-retrieve'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
