from django.urls import path
from .views import HomePageView
from .views import index
from .views import getinfo

urlpatterns = [
    # path('' , HomePageView , name = 'home'),
    path('' , index , name='index'),
    path('getinfo.html' , getinfo ,  name='getinfo' )
]