from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import House
from django.core.paginator import Paginator
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
    Post = House.objects.all().order_by('-post_creatDate')
    paginator = Paginator(Post, 4)
    page = request.GET.get('page')
    context = {
        'Posts':Post
    }
    return render(request, 'houses.html', context)    
def readMore(request, slug):
    house = House.objects.filter(houseId=slug).first()
    context = {
        'house':house,
    }
    return render(request, 'readMore.html', context)