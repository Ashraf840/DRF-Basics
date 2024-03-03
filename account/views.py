from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSignupSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair
from rest_framework.permissions import AllowAny

class UserSignupGenericView(generics.GenericAPIView):
    
    # NB: I can use "GenericAPIView" without using "ModelMixins"

    serializer_class=UserSignupSerializer
    permission_classes=[AllowAny]

    def post(self, request:Request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                "message":"User created successfully",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):

    permission_classes=[AllowAny]
    
    def post(self, request:Request):
        # TODO: This logic should be moved to a "LoginSerializer"
        email=request.data.get('email')
        password=request.data.get('password')
        user=authenticate(request, email=email, password=password)

        if user is not None:
            # Create JWT token
            tokens=create_jwt_pair(user)
            response={
                "message":"Login successful",
                "token":tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={"message":"Login failed"}, status=status.HTTP_401_UNAUTHORIZED)
