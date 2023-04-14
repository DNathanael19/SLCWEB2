from django.contrib import admin
from django.urls import path, include
from . import views
from .views import flight, salvar

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:flight_id>", flight, name="flight"), 
    path('salvar/', salvar, name='salvar'),
]