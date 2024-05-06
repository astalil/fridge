from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import RegisterNewUserSerializer, FridgeSerializer
from rest_framework.views import APIView
from django.db.models import Q
from fridge.models import Fridge

# Create your views here.

class RegisterUserView(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = RegisterNewUserSerializer

    def post(self, request, *args, **kwargs):
       
        print(request.data)
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

        user_fridges = Fridge.objects.filter(Q(owner=user) | Q(members=user)).distinct()
        fridge_data = FridgeSerializer(user_fridges, many=True, context={'request': request}).data
        print(fridge_data)
        #return JsonResponse({'fridges': fridge_data})

        data = {
            'user':
            {
                'id': user.pk,
                'email': user.email,
                'name': user.first_name,
                'surname': user.last_name
            },
            'fridges': fridge_data 
        }
        return Response(data)


# 
# from .models import User

# user = User.objects.get(email='testpeter.veliki@example.com')
# user_fridges = Fridge.objects.filter(Q(owner=user) | Q(members=user)).distinct()
# print(user_fridges)
# fridge_data = FridgeSerializer(user_fridges, many=True).data
# print(fridge_data)