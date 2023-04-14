from django.shortcuts import render
from .models import Iten, Lista, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "index.html", {
        "flights": Iten.objects.all()
    })

def flight(request, flight_id):
    flight = Iten.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "detalhes_lista.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })

def salvar(request):
    pass