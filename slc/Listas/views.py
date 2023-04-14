from django.shortcuts import render
from .models import Iten, Lista

# Create your views here.

def index(request):
    return render(request, "index.html", {
        "flights": Iten.objects.all()
    })