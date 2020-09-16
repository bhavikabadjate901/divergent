from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    url(r'^registration/',User_Regi.as_view()),
    url(r'^viewAll/',UserAllProfile.as_view()),
    url(r'^view/(?P<id>\d+)/$',User_Profile.as_view()),
    url(r'^edit/(?P<id>\d+)/$',Edit_User.as_view()),
    url(r'^delete_Account/(?P<id>\d+)/$',Delete_UserAccount.as_view()),
]