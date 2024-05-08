from django.urls import path
from .views import UserCreateView, Seller, UserListView, UserRetrieveView, UserUpdateView, UserDeleteView, LoginView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
    
    TokenVerifyView,
    
    TokenBlacklistView,
)

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user-retrieve'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
