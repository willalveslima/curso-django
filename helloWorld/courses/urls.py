from django.contrib import admin
from django.urls import path
from helloWorld.courses import views

urlpatterns = [
    path('', views.index, name ='index'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    path('<slug:slug>/', views.details , name ='details'),
    path('<slug:slug>/inscricao/', views.enrollment , name ='enrollment'),

]
