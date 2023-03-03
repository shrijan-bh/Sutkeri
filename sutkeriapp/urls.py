from django.contrib import admin

from django.urls import path
from sutkeriapp import views

urlpatterns = [
    path('', views.landing, name='landingpage'),
    path('services', views.services, name='services page'),
     path('contact', views.contact, name='contact page'),
     path('home', views.home, name='home page'),
     path('logoutpage', views.logoutpage, name='logoutpage'),
     path('login', views.loginpage, name='loginpage'),


     
   
]
