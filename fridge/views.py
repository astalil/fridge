from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from account.models import User
from django.db.models import Q
from account.serializers import FridgeSerializer
from django.forms.models import model_to_dict
from django.http import JsonResponse

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
        print(data)
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
            fridge = serializer.save()
            #user_fridges = Fridge.objects.filter(fridge)
            #fridge_data = FridgeSerializer(user_fridges, many=True, context={'request': request}).data
            fridge_data = {
                'id': fridge.pk,
                'name': fridge.name,
                'owner': request.user.pk,
                'items': [],
                'is_owner': True,
            }
        else:
            print(serializer.errors)
            return Response({'message': 'error', 'error': serializer.errors})
        
        return Response({'message': 'success', 'fridge': fridge_data })

class RemoveItemFromFridgeView(APIView):
    def post(self, request, *args, **kwargs):
        Item.objects.filter(pk__in = request.data['items']).delete()
        return Response({'message': 'success'})

class InvitationsView(APIView):
    def get(self, request):
        invites = Invitation.objects.filter(receiver = request.user, accepted = False, declined = False)
        serializer = InvitationSerilizer(invites, many=True).data
        
        print(serializer)
        return Response({'message': 'success', 'invites': serializer})
    
class InviteActionView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        invite = Invitation.objects.filter(pk = data['invite_id'], accepted= False, declined=False)
        if not invite.exists():
            return Response({'message': 'error', 'error': 'Invite does not exist'})
        
        invite=invite.first()
        if data['action'] == 'accept':
            invite.accepted = True
            fridge = Fridge.objects.filter(pk = invite.pk).first()
            fridge.members.add(request.user)
            serializer = FridgeSerializer(fridge, context={'request': request}).data
        else:
            invite.declined = True
            serializer = []
        invite.save()

        print(serializer)
        return Response({'message': 'success', 'fridge': serializer})
    
class GetItemsView(APIView):
    def get(self, request, *args, **kwargs):
        print(kwargs.get("fridge_id"))
        
        check_user = (Q(pk = kwargs.get("fridge_id")) & (Q(members__in = [request.user.pk]) | Q(owner = request.user)))
        fridge = Fridge.objects.filter(check_user)
        if not fridge.exists():
            print("errpr")
            return Response({'message': 'error', 'error': 'User has no access to this fridge!'})
        
        print(fridge)
        items = fridge.first().items.all().values("name", "quantity", "expiry_date")
        print(list(items))

        return JsonResponse({'message': 'success', 'items': list(items)})