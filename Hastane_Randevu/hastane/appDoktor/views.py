from django.shortcuts import render, redirect
from django.contrib.auth  import login, authenticate, logout
from django.contrib.auth.models  import User
from django.contrib import messages
from appSekreter.models import *
# Create your views here.

def loginDoktor(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        doktor = Doktor.objects.filter(slug = username, password=password)
        if doktor:
            return redirect('secreterDetay')
    return render(request, 'doktor/login.html')