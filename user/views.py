from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    
    RetrieveUpdateAPIView,
)
from .models import User
from .serializers import LoginSerializer, UserListSerializer, UserSerializer, UserUpdateSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
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
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
class UserUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'pk'
    
    
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
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
    
class LoginView(TokenObtainPairView):
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