from .models import User
from rest_framework import serializers
from fridge.models import Item, Fridge

from django.contrib.auth.forms import UserCreationForm 

class RegisterNewUserSerializer(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")
    

   


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'quantity', 'expiry_date']

class FridgeSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Fridge
        fields = ['id', 'name', 'owner', 'items', 'is_owner']

    def get_is_owner(self, obj):
        request = self.context.get('request')
        user = request.user if request else None
        print("Checking if the user is the owner: ", obj.owner == user)
        return obj.owner == user