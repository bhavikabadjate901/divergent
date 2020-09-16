from django.contrib import admin

# Register your models here.

from .models import Officer_Registration
 
class OfficerAdmin(admin.ModelAdmin):
    list_display = ['officerName','policeId','emailId'] 

# Register your models here.
admin.site.register(Officer_Registration,OfficerAdmin)