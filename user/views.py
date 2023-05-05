from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
# from models import User


class UserSignupView(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        otp = request.data.get('otp')
        name = request.data.get('name')

        # Check if mobile and otp are valid
        # Send OTP via SMS to mobile
        # Verify OTP

        user_data = {
            'mobile': mobile,
            'name': name,
            'otp': otp,
            'is_verified': True
        }

        serializer = UserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class UserSigninView(APIView):
    def post(self, request):
        mobile = request.data.get('mobile')
        otp = request.data.get('otp')

        # Check if mobile and otp are valid
        # Verify OTP

        user = User.objects.get(mobile=mobile)
        name = user.name

        return Response({'message': f'Welcome {name}'})
