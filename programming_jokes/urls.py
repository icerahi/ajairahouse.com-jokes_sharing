from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.programming_jokes,name='programming_jokes'),
    path('<int:pk>/',views.programming,name='programming'),
]
