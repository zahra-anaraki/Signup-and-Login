from django.shortcuts import render

from rest_framework import generics
from authentication.serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Create your views here.
