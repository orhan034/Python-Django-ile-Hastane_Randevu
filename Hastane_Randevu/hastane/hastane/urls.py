"""hastane URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *
from appHasta.views import *
from appSekreter.views import *
from appDoktor.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name='index'),
    # Hasta
    path('hastaLogin/',hastaLogin, name='hastaLogin'),
    path('hastaRegister/',hastaRegister, name='hastaRegister'),
    path('hastaDetay/',hastaDetay, name='hastaDetay'),
    path('logouthastaUser/',logouthastaUser, name='logouthastaUser'),
    # Sekreter
    path('secreterLogin/',secreterLogin, name='secreterLogin'),
    path('secreterRegister/',secreterRegister, name='secreterRegister'),
    path('secreterDetay/',secreterDetay, name='secreterDetay'),
    path('duyuru/',DuyuruFon, name='DuyuruFon'),
    path('randevuListe/',randevuListe, name='randevuListe'),
    path('BransPaneli/',BransPaneli, name='BransPaneli'),
    # doktor
    path('doktor/',doktor, name='doktor'),
    path('loginDoktor/',loginDoktor, name='loginDoktor'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
