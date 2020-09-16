from .models import Officer_Registration
from rest_framework import serializers


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer_Registration
        fields = ['name','password']

class OfficerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Officer_Registration
        fields = '__all__'