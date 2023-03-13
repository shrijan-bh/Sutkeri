from django.contrib import admin

from django.urls import path
from sutkeriapp import views

urlpatterns = [
    path('', views.landing, name='landingpage'),
    path('services', views.services, name='services page'),
     path('contact', views.contact, name='contact page'),
     path('home1', views.home1, name='home1 page'),
     path('home2', views.home2, name='home2 page'),
     path('home3', views.home3, name='home3 page'),

     path('logoutpage', views.logoutpage, name='logoutpage'),
     path('login', views.loginpage, name='login'),   
     path('kyc',views.kyc,name="kyc page"),
     path('healthdata',views.healthdata,name="healthdata page"),



   
]
