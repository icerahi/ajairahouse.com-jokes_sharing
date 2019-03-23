from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.bangla_jokes,name='bangla_jokes'),
    path('<int:pk>/',views.bangla,name='bangla'),
]
