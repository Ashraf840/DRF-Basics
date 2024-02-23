from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSignupSerializer
from rest_framework.request import Request
from rest_framework.response import Response

class UserSignupGenericView(generics.GenericAPIView):
    
    # NB: I can user "GenericAPIView" without using "ModelMixins"

    serializer_class=UserSignupSerializer

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

