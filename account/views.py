from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import RegisterNewUserSerializer
from rest_framework.views import APIView
# Create your views here.

class RegisterUserView(CreateAPIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
       
        serializer = RegisterNewUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            message = "success"
            errors = []
        else:
            message = 'error'
            errors = serializer.errors
            print(serializer.errors)
        
        return Response({"status": message, "errors": errors})

class UserDataView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)

        data = {
            'id': user.pk,
            'email': user.email,
            'name': user.first_name
        }
        return Response(data)
    