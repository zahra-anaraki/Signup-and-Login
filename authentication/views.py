from django.shortcuts import render

from rest_framework import generics
from authentication.serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt
from django.conf import settings
from datetime import datetime, timedelta

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "کاربری با این ایمیل یافت نشد."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if user is not None:
            payload = {
                "id": user.id,
                "exp": datetime.utcnow() + timedelta(days=1),
                "iat": datetime.utcnow(),
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

            return Response({"token": token}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "رمز عبور اشتباه است."}, status=status.HTTP_401_UNAUTHORIZED)


