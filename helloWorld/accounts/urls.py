from django.contrib import admin
from django.contrib.auth import views as v_auth
from django.urls import path,re_path
from helloWorld.accounts import views


urlpatterns = [
    #path('entrar', v_auth.LoginView,{'template_name':'accounts/login.html'}, name = 'login' ),
    path('', views.dashboard, name = 'dashboard' ),
    path('entrar', v_auth.LoginView.as_view(), name = 'login' ),
    path('sair', v_auth.LogoutView.as_view(), name = 'logout' ),
    path('cadastra-se', views.register, name = 'register' ),
    path('nova-senha', views.password_reset, name = 'password_reset' ),
    re_path(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.password_reset_confirm, name = 'password_reset_confirm' ),
    path('editar', views.edit, name = 'edit' ),
    path('editar-senha', views.edit_password, name = 'edit_password' )

]
