from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, "index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight= Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    return render(request, "flight.html", {
        "flight": flight,
        "passengers": passengers
    })