from .models import Login
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LoginSerializer, SignupSerializer, InformationSerializer, IdentifySerializer

class SignupCreate(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = SignupSerializer


class LoginListCreate(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

