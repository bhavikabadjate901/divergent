from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from .serializers import OfficerSerializer,loginSerializer
from rest_framework.response import Response
import json
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
#from django_otp.oath import TOTP
# import time,datetimes
#from django_otp.util import random_hex
from random import randrange
#from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage  
#for communicaton with other services
import requests
from .models import Officer_Registration
from rest_framework import status


class Officer_Regi(APIView):
    @csrf_exempt
    def post(self,request, format=None):
        if request.method == 'POST':
            
            payload =json.loads(request.body)
            print(payload)
            offiserName = payload['offiserName']
            policeId = payload['policeId']
            rank = payload['rank']
            retiredDate = payload['retiredDate']
            dateOfHier = payload['dateOfHier']
            policeStation = payload['policeStation']
            pincode = payload['pincode']
            state = payload['state']
            country = payload['country']
            district = payload['district']
            dateOfBirth = payload['dateOfBirth']
            gender = payload['gender']
            emailId = payload['emailId']
            password = payload['password']
            confirmPassword = payload['confirmPassword']
            Role = payload['Role']
            officer = Officer_Registration(offiserName = offiserName, policeId = policeId, rank = rank, retiredDate = retiredDate, dateOfHier = dateOfHier, policeStation = policeStation, pincode = pincode, state = state, country = country, district = district, dateOfBirth = dateOfBirth, gender = gender,emailId = emailId, password = password , confirmPassword = confirmPassword)
            # try:
            officer.save()
            response = json.dumps([{'Success':'Added'}])
            #except:    
            response = json.dumps([{'Error':'Error! Not added'}])
        return HttpResponse(response, content_type='text/json')


class OfficerAllProfile(APIView):
    @csrf_exempt
    def get(self,request):
        registration=Officer_Registration.objects.all()
        serializer1=OfficerSerializer(registration,many=True)
        # print(serializer1.data)
        response = json.dumps(serializer1.data)
        return HttpResponse(response, content_type='text/json')  


class Officer_Profile(APIView):
    def get_object(self,id):
        try:
            return Officer_Registration.objects.get(id=id)
        except Officer_Registration.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
     
    def get(self,request,id):
        temp=self.get_object(id)
        serializer1=OfficerSerializer(temp)
        return Response(serializer1.data) 


class Edit_Officer(APIView):
    @csrf_exempt
    def put(self,request,id, format=None):
        if request.method == 'PUT':
            try:
                officer=Officer_Registration.objects.get(id=id)
                data = JSONParser().parse(request)
                serializer=OfficerSerializer(officer, data=data)
                if serializer.is_valid():
                    serializer.save()
                    # return JsonResponse(serializer.data,safe=False)
                    response = json.dumps([{'Success':'Added'}])
            except:
                response = json.dumps([{'Error':'Error! Not added'}])
        return HttpResponse(response, content_type='text/json')



class Delete_OfficerAccount(APIView):
    @csrf_exempt
    def get_object(self,id):
        try:
            return Officer_Registration.objects.get(id=id)
        except Officer_Registration.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
     
    def get(self,request,id):
        temp=self.get_object(id)
        serializer1=OfficerSerializer(temp)
        return Response(serializer1.data)

    def delete(self,request,id):
        temp=self.get_object(id)
        temp.delete()
        print("deleted")
        return Response([{'Success':'deleted'}])

