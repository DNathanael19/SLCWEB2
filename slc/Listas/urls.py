from django.contrib import admin
from django.urls import path, include
from .views import flight, newlist, index, newlist2, editar, update, delete

urlpatterns = [
    path('', index, name="index"),
    path("<int:flight_id>", flight, name="flight"), 
    path('newlist/', newlist, name='newlist'),
    path('newlist2/', newlist2, name='newlist2'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]