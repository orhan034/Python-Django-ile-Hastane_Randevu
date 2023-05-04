from django.shortcuts import render, redirect
from django.contrib.auth  import login, authenticate, logout
from django.contrib.auth.models  import User
from .models import *
from appSekreter.models import *
# Create your views here.

def hastaLogin(request):
    context = {}
    if request.method == "POST":
        if request.POST.get("button")=="buttonGiris":
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username = username, password=password)
            if user is not None:
                login(request,user)
                return redirect('hastaDetay')
            else:
                hata = "Kullanıcı adı veya şifre yanlış!"
                context.update({"hata":hata})

    return render(request, 'hasta/hastalogin.html', context)

def hastaRegister(request):
    context = {}
    if request.method == "POST":
        if request.POST.get("button")=="buttonkayit":
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            email = request.POST.get("email")
            username = request.POST["username"]
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            
            if password1==password2:
                user = User.objects.create_user(username=username, 
                                                password=password1,
                                                email=email, 
                                                last_name = name, 
                                                first_name = surname)   
                user.save()

                hastauserinfo = HastaUserInfo(user=user, password=password1)
                hastauserinfo.save()

                return redirect("hastaLogin")
            else:
                hata = "Şifreler aynı değil"
                context.update({"hata": hata})
           


    return render(request, 'hasta/hastaregister.html', context)

def hastaDetay(request):
    user = User.objects.get(username = request.user)
    hastauserinfo = HastaUserInfo.objects.get(user = user)
    randevu = RandevuBrans.objects.all()
    branslar = Brans.objects.all()
    doktorlar = Doktor.objects.all()
    if request.method == "POST":
        if request.POST.get("button")=="buttonProfil":
            password = request.POST["password"]
            if user.check_password(password):
                name = request.POST.get("name")
                surname = request.POST.get("surname")
                tcno = request.POST.get("tcno")
                username = request.POST.get("username")
                phone = request.POST.get("phone")
                cinsiyet = request.POST.get("cinsiyet")
                user.username = username
                user.save()
                hastauserinfo.isim = name
                hastauserinfo.soyad = surname
                hastauserinfo.hastaTC = tcno
                hastauserinfo.hastaTelefon = phone
                hastauserinfo.cinsiyet = cinsiyet
                hastauserinfo.save()
                return redirect("hastaDetay")
        
        if request.POST['button'] == 'buttonSifre':
            password = request.POST['password']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            user = User.objects.get(username = request.user)
            if user.check_password(password):
                if password2==password1:
                    user.set_password(password1)
                    user.save()
                    logout(request) 
                    return redirect("hastaDetay")
                
        # Randevu İşlemleri
        if request.method == 'POST':
            if request.POST.get('button')=='randebuAl':
                # randevuid = request.POST.get('randevuid')
                # rand = RandevuBrans.objects.get(id = randevuid)
                brans_id = request.POST.get('brans')
                brans = RandevuBrans.objects.get(randevuDoktor__slug = brans_id)
                doktor_id = request.POST.get('doktor')
                doktor = Doktor.objects.get(slug = doktor_id)
                text = request.POST.get('text')

                rndv = RandevuBrans.objects.filter(randevuBrans__slug = brans,
                                                   randevuDoktor__slug = doktor)
                
                print("===============",rndv)
                hastaRan = HastaRandevu(user = request.user, randevu = rndv, text = text)
                print("============",hastaRan)
                hastaRan.save()
                return redirect("hastaDetay")



    context = {
        "hastauserinfo":hastauserinfo,
        'randevu':randevu,
        'branslar':branslar,
        'doktorlar':doktorlar,
    }
    return render(request, 'hasta/hastadetay.html',context)

def logouthastaUser(request):
    logout(request)
    return redirect('index')