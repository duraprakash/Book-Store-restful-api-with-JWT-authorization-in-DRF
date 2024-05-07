from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import User
from .serializers import UserSerializer, UserListSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        token = get_tokens_for_user(user)
        
        return Response({'token':token, 'msg':'SignUp Successful'}, status=status.HTTP_201_CREATED)
    
class Seller(ListAPIView):
    serializer_class = UserListSerializer
    
    def get_queryset(self):
        return User.objects.filter(seller=True)
    
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Serialize the old object before updating
        old_data = UserListSerializer(instance).data

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response({'old_data': old_data, 'new_data': serializer.data}, status=status.HTTP_200_OK)
    
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    

class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'error': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    
class LoginView(APIView):
    serializers_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)