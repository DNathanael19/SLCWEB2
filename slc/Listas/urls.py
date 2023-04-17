from django.contrib import admin
from django.urls import path
from .views import flight, newlist, index, newlist2, newlist3, editar, update, delete, cadastro, login, logout_view, delete2

urlpatterns = [
    path('', index, name="index"),
    path("<int:flight_id>", flight, name="flight"), 
    path('newlist/', newlist, name='newlist'),
    path('newlist2/', newlist2, name='newlist2'),
    path('newlist3/', newlist3, name='newlist3'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('delete2/<int:id>', delete2, name='delete2'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path("logout", logout_view, name="logout"),
]