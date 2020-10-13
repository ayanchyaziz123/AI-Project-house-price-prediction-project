from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')
def contactUs(request):
    return render(request, 'contactUs.html')    
def aboutUs(request):
    return render(request, 'aboutUs.html') 