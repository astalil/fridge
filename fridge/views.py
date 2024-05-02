from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from account.models import User

# Create your views here.
class CreateFridge(APIView):
    def post(self, request):

        user = request.user
        serializer = CreateFridgeSerializer(request.data, context={'user': user})
        if serializer.is_valid():
            serializer.save()
        
        else:
            return Response({'message': 'error', 'errors': serializer.errors})

        return Response({'message': 'success'})
    

class AddItemToFridgeView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        data['fridge'] = kwargs.get("fridge_id")

        serializer = AddNewItemSerilaizer(data=data)
        if serializer.is_valid():
            item = serializer.save()
            data['id'] = item.pk
            
        else:
            print(serializer.errors)
            return Response({'message': 'error', 'errors': serializer.errors})

        return Response({'message': 'success', 'item': data})

class InvitePeopleView(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        user = User.objects.filter(email = data['receiver'])
        if not user.exists():
            return Response({'message': 'error', 'error': 'User with this email does not exist'})
        
        data['sender'] = request.user.pk
        data['receiver'] = user.first().pk
        print(data)
        serializer = SendInvitationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
            return Response({'message': 'error', 'error': serializer.errors})

        return Response({'message': 'sucess'})
    
class AddNewFridgeView(APIView):
    def post(self, request):
        data = request.data
        data['owner'] = request.user.pk
        print(data)
        serializer = AddFridgeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
            return Response({'message': 'error', 'error': serializer.errors})

        return Response({'message': 'success'})