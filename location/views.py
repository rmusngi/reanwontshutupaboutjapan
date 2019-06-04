from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import destination

def index(request):
    locations = destination.objects.all()
    context = {
        'locations' : locations
    }
    return render(request, 'location/location.html', context)

def city(request, destination_id):
    city = get_object_or_404(destination, pk=destination_id)
    context = {
        'city' : city
    }
    return render(request, 'location/destination.html', context)
    