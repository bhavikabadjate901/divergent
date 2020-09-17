from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from .models import User_Registration
from .serializers import UserSerializer,loginSerializer
from rest_framework.response import Response
import json
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
#from django_otp.oath import TOTP
import time,datetime
#from django_otp.util import random_hex
from random import randrange
#from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage  
#for communicaton with other services
import requests
from .models import User_Registration
from rest_framework import status


class User_Regi(APIView):
    
    @csrf_exempt
    def post(self,request, format=None):
        if request.method == 'POST':
            
            payload =json.loads(request.body)
            print(payload)
            name = payload['name']
            phoneNo = payload['phoneNo']
            address = payload['address']
            emailId = payload['emailId']
            password = payload['password']
            confirmPassword = payload['confirmPassword']
            state = payload['state']
            pincode = payload['pincode']
            district = payload['district']
            country = payload['country']
            gender = payload['gender']
            dateOfBirth = payload['dateOfBirth']
            aadharNo= payload['aadharNo']
            if password == confirmPassword:
                user = User_Registration(name=name,phoneNo=phoneNo,address=address,emailId= emailId,password= password, 
                confirmPassword=confirmPassword,state=state,pincode=pincode,district=district,country=country,gender=gender,
                dateOfBirth=dateOfBirth,aadharNo=aadharNo)
            #try:
                user.save()
                response = json.dumps([{'Success':'Added'}])
            else:
            #except:    
                response = json.dumps([{'Error':'Error! Not added'}])
        return HttpResponse(response, content_type='text/json')


class UserAllProfile(APIView):
    @csrf_exempt
    def get(self,request):
        registration=User_Registration.objects.all()
        serializer1=UserSerializer(registration,many=True)
        # print(serializer1.data)
        response = json.dumps(serializer1.data)
        return HttpResponse(response, content_type='text/json')  


class User_Profile(APIView):
    def get_object(self,id):
        try:
            return User_Registration.objects.get(id=id)
        except User_Registration.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
     
    def get(self,request,id):
        temp=self.get_object(id)
        serializer1=UserSerializer(temp)
        return Response(serializer1.data) 


class Edit_User(APIView):
    @csrf_exempt
    def put(self,request,id, format=None):
        if request.method == 'PUT':
            try:
                user=User_Registration.objects.get(id=id)
                data = JSONParser().parse(request)
                serializer=UserSerializer(user, data=data)
                if serializer.is_valid():
                    serializer.save()
                    # return JsonResponse(serializer.data,safe=False)
                    response = json.dumps([{'Success':'Added'}])
            except:
                response = json.dumps([{'Error':'Error! Not added'}])
        return HttpResponse(response, content_type='text/json')



class Delete_UserAccount(APIView):
    @csrf_exempt
    def get_object(self,id):
        try:
            return User_Registration.objects.get(id=id)
        except User_Registration.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
     
    def get(self,request,id):
        temp=self.get_object(id)
        serializer1=UserSerializer(temp)
        return Response(serializer1.data)

    def delete(self,request,id):
        temp=self.get_object(id)
        temp.delete()
        print("deleted")
        return Response([{'Success':'deleted'}])


