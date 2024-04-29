from .models import User
from rest_framework import serializers

from django.contrib.auth.forms import UserCreationForm 

class RegisterNewUserSerializer(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")
    
    def validate(self, data):
       if data['password1'] != data['password2']:
           raise serializers.ValidationError("passwords not the same")
       
       return data