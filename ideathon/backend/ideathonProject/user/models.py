from django.db import models

# Create your models here.
class User_Registration(models.Model):
    
    name = models.CharField(max_length=100)
    phoneNo = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=50,default="null")
    emailId = models.EmailField(max_length=100)
    state = models.CharField(max_length=50,default="null")
    password = models.CharField(max_length=100)
    confirmPassword = models.CharField(max_length=100)
    aadharNo= models.BigIntegerField(unique=True)
    gender=models.CharField(max_length=100,default="null")
    pincode=models.IntegerField()
    district=models.CharField(max_length=50,default="null")
    country=models.CharField(max_length=100,default="null")
    dateOfBirth=models.DateField(max_length=50,default="2000-05-21")
    
    def __str__(self):
        return self.name



