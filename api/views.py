from django.contrib.auth import get_user_model
from rest_framework import generics, status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from .models import FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer
from api import models
from django.db.models import Q


User = get_user_model()

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        # print(f"Email: {email}, Password: {password}")
        user = User.objects.filter(email__iexact=email).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username', 'email']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

class SendFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        to_user_id = request.data.get('to_user')
        to_user = User.objects.get(id=to_user_id)
        friend_request, created = FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user, status='pending')
        if created:
            return Response({'status': 'Friend request sent'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Friend request already sent'}, status=status.HTTP_200_OK)

class AcceptFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, *args, **kwargs):
        friend_request = FriendRequest.objects.get(id=pk, to_user=request.user)
        friend_request.status = 'accepted'
        friend_request.save()
        return Response({'status': 'Friend request accepted'}, status=status.HTTP_200_OK)

class RejectFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, *args, **kwargs):
        
        friend_request = FriendRequest.objects.get(id=pk, to_user=request.user)
        friend_request.status = 'rejected'
        friend_request.save()
        return Response({'status': 'Friend request rejected'}, status=status.HTTP_200_OK)


class ListFriendsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(Q(sent_requests__to_user=user, sent_requests__status='accepted') | Q(received_requests__from_user=user, received_requests__status='accepted')).distinct()


class ListPendingRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')
