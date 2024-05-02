from .models import Fridge, Item, Invitation
from account.models import User
from rest_framework import routers, serializers, viewsets

class CreateFridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        fields = ('name')

class AddNewItemSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'quantity', 'expiry_date', 'fridge')

    def create(self, validated_data):
        item = Item.objects.create(**self.validated_data)
        return item

class SendInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('sender', 'receiver', 'fridge')
    

    def create(self, validated_data):
        item = Invitation.objects.create(**self.validated_data)
        return item
    
class AddFridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        fields = ('name', 'owner')

    def create(self, velidated_data):
        fridge = Fridge.objects.create(**self.validated_data)
        return fridge