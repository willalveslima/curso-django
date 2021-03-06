"""helloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
import helloWorld.home
import helloWorld.courses


urlpatterns = [
    path('', include(('helloWorld.home.urls','home') , namespace= 'home')),
    path('cursos/', include(('helloWorld.courses.urls','courses') , namespace= 'courses')),
    path('contas/', include(('helloWorld.accounts.urls','accounts') , namespace= 'accounts')),
    path('forum/', include(('helloWorld.forum.urls','forum') , namespace= 'forum')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)