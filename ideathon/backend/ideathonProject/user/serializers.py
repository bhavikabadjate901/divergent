from .models import User_Registration
from rest_framework import serializers


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model =User_Registration
        fields = ['name','password']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = User_Registration
        fields = '__all__'