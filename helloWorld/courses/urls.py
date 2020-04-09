from django.contrib import admin
from django.urls import path
from helloWorld.courses import views

urlpatterns = [
    path('', views.index, name ='index'),
    # url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    path('<slug:slug>/', views.details , name ='details'),
    path('<slug:slug>/inscricao/', views.enrollment , name ='enrollment'),
    path('<slug:slug>/cancelar-inscricao/', views.undo_enrollment , name ='undo_enrollment'),
    path('<slug:slug>/anuncios/', views.announcements , name ='announcements'),
    path('<slug:slug>/anuncios/<int:pk>', views.show_announcement , name ='show_announcement'),
    path('<slug:slug>/aulas/', views.lessons , name ='lessons'),
    path('<slug:slug>/aulas/<int:pk>', views.lesson , name ='lesson'),
    path('<slug:slug>/materiais/<int:pk>', views.material , name ='material'),
]
