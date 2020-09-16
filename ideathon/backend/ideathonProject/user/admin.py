from django.contrib import admin
from .models import User_Registration
 
# Register your models here.
# admin.site.register(User_Registration)

class userAdmin(admin.ModelAdmin):
    list_display=['id','name','phoneNo','address','state','pincode','district','country',
    'emailId','aadharNo','gender','dateOfBirth','password']

admin.site.register(User_Registration,userAdmin)