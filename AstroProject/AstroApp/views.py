from django.shortcuts import render
import json
import turtle
import urllib.request
import time
import geocoder

# Create your views here.

def home(request):
    return render(request, 'home.html')

