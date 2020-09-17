from django.db import models

# Create your models here.
class Officer_Registration(models.Model):
    officerName = models.CharField(max_length=56)
    policeId = models.CharField(max_length=40)
    rank = models.IntegerField()
    retiredDate = models.DateField()
    dateOfHier = models.DateField()
    policeStation = models.CharField(max_length=100)
    pincode = models.IntegerField()
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    emailId = models.EmailField()
    password = models.CharField(max_length=64)
    confirmPassword = models.CharField(max_length=64)


    def __str__(self):
        return self.officerName
