from django.urls import path
from helloWorld.forum import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('tag/<str:tag>/', views.index , name ='index_tagged'),
    path('respostas/<int:pk>/correta/', views.reply_correct , name ='reply_correct'),
    path('respostas/<int:pk>/incorreta/', views.reply_incorrect , name ='reply_incorrect'),
    path('<slug:slug>/', views.thread , name ='thread'),
    
]
