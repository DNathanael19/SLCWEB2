from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Iten, Lista, Passenger
from django.urls import reverse
from .forms import ListForm, ListForm2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
# Create your views here.


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Ja existe um usuario com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponseRedirect(reverse("login"))




def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "login.html", {
                            "message": "Invalid Credentials"
                        })
        
def logout_view(request):
    logout(request)
    return render(request, "login.html", {
                "message": "Logged Out"
            })



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
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

def delete2(request, id):
    app = Iten.objects.get(id=id)
    app.delete()
    return redirect(index)