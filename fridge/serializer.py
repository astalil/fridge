from .models import Fridge
from rest_framework import routers, serializers, viewsets

class FridgeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Fridge
        fields = ['name', 'items']