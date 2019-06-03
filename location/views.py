from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'location/location.html')

def destination(request):
    return render(request, 'location/destination.html')
    