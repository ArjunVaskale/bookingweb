from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .models import GetInfo

# Create your views here.
from django.template import loader
from django.http import HttpResponse

def HomePageView(request):
    return HttpResponse('hello world')

def index(request):
    lname = 'vaskale'
    name = {
        'fname' : lname
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(name))

@csrf_exempt
def getinfo(request):
    if request.method == 'POST':
        value = request.POST.get('email')
        person  = GetInfo()
        person.name = request.POST.get('name')
        person.email = request.POST.get('email')
        person.aadhar = request.POST.get('aadhar')
        person.hotelname = request.POST.get('hotel')
        person.mobile = request.POST.get('mobile')
        person.datetime = request.POST.get('datetime')
        person.save()
        data = {
                'email': value  
        }
        

        template = loader.get_template('index.html' )

        return HttpResponse(template.render(data))

    else:
        template = loader.get_template('getinfo.html')
        return HttpResponse(template.render())


