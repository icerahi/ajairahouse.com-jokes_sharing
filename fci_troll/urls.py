from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fci_troll,name='fci_troll'),
    path('<int:pk>/',views.fci,name='fci'),
]
