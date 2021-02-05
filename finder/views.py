import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    response = requests.get('http://freegeoip.app/json/')
    geodata = response.json()
    return render(request, "index.html", {
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude']
    })

def about(request):
    return render(request, "about.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
