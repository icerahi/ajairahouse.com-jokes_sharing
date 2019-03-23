from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.engineering_jokes,name='engineering_jokes'),
    path('<int:pk>/',views.engineer,name='engineer'),
]
