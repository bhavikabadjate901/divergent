from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

from django.conf import settings
from django.conf.urls import url



urlpatterns = [
    url(r'^registration/',Officer_Regi.as_view()),
    url(r'^viewAll/',OfficerAllProfile.as_view()),
    url(r'^view/(?P<id>\d+)/$',Officer_Profile.as_view()),
    url(r'^edit/(?P<id>\d+)/$',Edit_Officer.as_view()),
    url(r'^delete_Account/(?P<id>\d+)/$',Delete_OfficerAccount.as_view()),
]

