from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import House

# Create your views here.

def home(request):
    house = House.objects.all().order_by('-post_creatDate')[0:4]
    context = {
        'house':house
    }
    return render(request, 'home.html', context)
def contactUs(request):
    return render(request, 'contactUs.html')    
def aboutUs(request):
    return render(request, 'aboutUs.html') 
def houses(request):
    return render(request, 'houses.html')    
