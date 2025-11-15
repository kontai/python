from django.contrib import admin
from django.urls import path,include
from app02 import views

urlpatterns = [
    path('index',views.index),
    path('index2', views.index2),
]