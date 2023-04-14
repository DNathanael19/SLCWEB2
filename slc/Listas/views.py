from django.shortcuts import render
from .models import Iten, Lista

# Create your views here.

def index(request):
    return render(request, "index.html", {
        "flights": Iten.objects.all()
    })

def flight(request, flight_id):
    flight = Iten.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    return render(request, "detalhes_lista.html", {
        "flight": flight,
        "passengers": passengers
    })