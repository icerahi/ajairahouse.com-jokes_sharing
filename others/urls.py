from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('privacypolicy/',views.policy,name='policy'),
    path('terms',views.terms,name='terms'),
    path('contact/',views.contact,name='contact'),
]
