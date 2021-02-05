import requests
from django.shortcuts import render
from django.http import HttpResponse

from finder.utils import get_location, get_barbers, get_client_ip
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    ip = get_client_ip(request)
    latitude, longitude = get_location(ip)
    businesses = get_barbers(latitude, longitude)['businesses']
    return render(request, "index.html", {'business': businesses})

def about(request):
    return render(request, "about.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
