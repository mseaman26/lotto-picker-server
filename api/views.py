from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import LottoPick
from .serializers import LottoPickSerializer, UserSerializer

class LottoPickViewSet(viewsets.ModelViewSet):
    queryset = LottoPick.objects.all()
    serializer_class = LottoPickSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Retrieve all users
    serializer_class = UserSerializer  # Use your UserSerializer for serialization

    def perform_create(self, serializer):
        # Save the user instance using the serializer
        serializer.save()
