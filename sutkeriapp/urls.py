from django.contrib import admin
from django.urls import path, include
from sutkeriapp import views

urlpatterns = [
    path('', views.landing, name='landing page'),
    path('services', views.services, name='services page'),
     path('contact', views.contact, name='contact page'),
]
