from django.shortcuts import render
import json
import turtle
import urllib.request
import time
import geocoder

# Create your views here.
def home(request):
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    astronauts = result['number']
    context = {'astronauts':astronauts}
    return render(request, 'home.html', context)
