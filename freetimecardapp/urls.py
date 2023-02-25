from django.contrib import admin
from django.urls import path, include
from . import views

## HERE WE ARE SETTING THE URLS FOR OUT PROJECT
urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout")
]