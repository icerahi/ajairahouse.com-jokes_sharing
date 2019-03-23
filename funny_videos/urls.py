from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.funny_videos,name='funny_videos'),
    path('<int:pk>/',views.funny,name='funny'),
]
