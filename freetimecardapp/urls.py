from django.contrib import admin
from django.urls import path, include
from . import views

## HERE WE ARE SETTING THE URLS FOR OUT PROJECT
urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('clock_in', views.clock_in, name="clock_in"),
    path('clock_out', views.clock_out, name="clock_out"),
    path('clock_history', views.clock_history, name="clock_history")
]