from django.shortcuts import render, redirect
from .models import Iten, Lista, Passenger
from django.urls import reverse
from .forms import ListForm, ListForm2

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




def newlist(request):
    if request.method == 'POST':
        form = ListForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect(index)
    else:
        form = ListForm()
        return render(request, 'newlist.html', {'form':form})




def newlist2(request):
    if request.method == 'POST':
        form2 = ListForm2(request.POST)

        if form2.is_valid():
            task2 = form2.save(commit=False)
            task2.save()
            return redirect(index)
    else:
        form2 = ListForm2()
        return render(request, 'newlist2.html', {'form':form2})
    
    


def editar(request, id):
    app = Passenger.objects.get(id=id)
    return render(request, 'update.html', {'app': app})




def update(request, id):
    vnome = request.POST.get("nome")
    app = Passenger.objects.get(id=id)
    app.first = vnome
    app.save()
    return redirect(index)




def delete(request, id):
    app = Passenger.objects.get(id=id)
    app.delete()
    return redirect(index)