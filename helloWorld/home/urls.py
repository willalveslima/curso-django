from django.contrib import admin
from django.urls import path
from helloWorld.home import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('contato/', views.contacts , name ='contacts'),
]
