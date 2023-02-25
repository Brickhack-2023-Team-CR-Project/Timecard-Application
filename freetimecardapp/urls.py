from django.contrib import admin
from django.urls import path, include
from . import views

## HERE WE ARE SETTING THE URLS FOR OUT PROJECT
urlpatterns = [
    path('', views.home, name="home")
]