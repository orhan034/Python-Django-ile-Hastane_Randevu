from django.shortcuts import render, redirect
from django.contrib.auth  import login, authenticate, logout
from django.contrib.auth.models  import User
from django.contrib import messages
from .models import *
# Create your views here.

def secreterLogin(request):
    context = {}
    if request.method == "POST":
        if request.POST.get("button")=="buttonGiris":
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username = username, password=password)
            if user is not None:
                login(request,user)
                return redirect('secreterDetay')
            else:
                hata = "Kullanıcı adı veya şifre yanlış!"
                context.update({"hata":hata})

    return render(request, 'sekreter/secreterlogin.html')

def secreterRegister(request):
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

                hastauserinfo = secreterUserInfo(user=user, password=password1)
                hastauserinfo.save()

                return redirect("secreterLogin")
            else:
                hata = "Şifreler aynı değil"
                context.update({"hata": hata})
    return render(request, 'sekreter/secreterregister.html')

def secreterDetay(request):
    user = User.objects.get(username = request.user)
    secreteruserinfo = secreterUserInfo.objects.get(user = user)
    bransgetir = Brans.objects.all()
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
                secreteruserinfo.isim = name
                secreteruserinfo.soyad = surname
                secreteruserinfo.secreterTC = tcno
                secreteruserinfo.hastaTelefon = phone
                secreteruserinfo.cinsiyet = cinsiyet
                secreteruserinfo.save()
                return redirect("secreterDetay")
        
        if request.POST.get('button') == 'buttonSifre':
            password = request.POST['password']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            user = User.objects.get(username = request.user)
            if user.check_password(password):
                if password2==password1:
                    user.set_password(password1)
                    user.save()
                    logout(request) 
                    return redirect("secreterDetay")
         
        if request.POST.get("button")=="bransEkle":
            date = request.POST.get("date")
            time = request.POST.get("time")
            brans_id = request.POST.get("branslar")
            branss = Brans.objects.get(slug = brans_id)
            doktor_id = request.POST.get("doktor")
            doktor = Doktor.objects.get(slug = doktor_id)
            if RandevuBrans.objects.filter(randevuSaat = time) and RandevuBrans.objects.filter(randevuDoktor = doktor):
                pass
            else:
                bransekle = RandevuBrans.objects.create(randevuTarih = date,
                                                    randevuSaat = time,
                                                    randevuBrans = branss,
                                                    randevuDoktor = doktor,
                                                    )
                bransekle.save()

        if request.POST.get('button')=='duyuruEkle':
            text = request.POST.get('text')    
            duyuru = Duyuru(duyuru = text)
            duyuru.save()
            return redirect("secreterDetay")
    context = {
        "secreteruserinfo":secreteruserinfo,
        'bransgetir':bransgetir,
        'doktorlar':doktorlar,
    }
    return render(request, 'sekreter/secreterdetay.html', context)

def doktor(request):
    branslar = Brans.objects.all()
    doktorlar = Doktor.objects.all()
    if request.method == "POST":
        if request.POST.get("button")=="buttonkayit":
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            brans_id = request.POST.get("bransll")
            brans = Brans.objects.get(id = brans_id)
            tcno = request.POST.get("tcno")
            password = request.POST.get("password")

            doktorekle = Doktor.objects.create(isim = name,
                                                soyad = surname,
                                                password=password,
                                                doktorBrans=brans,
                                                doktorTC=tcno)
            doktorekle.save()
            return redirect("doktor")
        if request.POST.get("button")=="buttonDoktorGuncelle":
            doktorid = request.POST.get("doktorid")
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            tcno = request.POST.get("tcno")
            bransguncel_id = request.POST.get("bransguncel")
            brans = Brans.objects.get(id = bransguncel_id)
            password = request.POST.get("password")
            doktorGucel = Doktor.objects.get(id = doktorid)
            doktorGucel.isim = name
            doktorGucel.soyad = surname
            doktorGucel.doktorBrans = brans
            doktorGucel.doktorTC = tcno
            doktorGucel.password = password
            doktorGucel.save()
             
        if request.POST.get("button")=="buttonDoktorSil":
            doktorid = request.POST.get("doktorid")
            doktorSil = Doktor.objects.get(id = doktorid)
            doktorSil.delete()
            return redirect("doktor")
    context = {
       'branslar':branslar,
       'doktorlar':doktorlar,
    }
    return render(request, "sekreter/doktor.html", context)

def DuyuruFon(request):
    duyuru = Duyuru.objects.all()
    if request.method == "POST":
        if request.POST.get("button")=="buttonkayit":
            duyuruid = request.POST.get("duyuruid")
            text = request.POST.get("text")
            try:
                duyuruGuncel = Duyuru.objects.get(id = duyuruid)
                duyuruGuncel.duyuru = text
                duyuruGuncel.save()
                return redirect('DuyuruFon')
            except:
                messages.warning(request, 'Böyle İd Bulunmamaktadır')
                return redirect('DuyuruFon')
        if request.POST.get("button")=="buttonDuyuruSil":
            duyuruid = request.POST.get("duyuruid")
            try:
                duyuruSil = Duyuru.objects.get(id = duyuruid)
                duyuruSil.delete()
                return redirect("DuyuruFon")
            except:
                messages.warning(request, 'Böyle İd Bulunmamaktadır')
                return redirect('DuyuruFon')            
    context = {
        'duyuru':duyuru,
    }
    return render(request, 'sekreter/duyuru.html',context)


def randevuListe(request):
    randevuliste = RandevuBrans.objects.all()
    branslar = Brans.objects.all()
    doktorlar = Doktor.objects.all()
    if request.method == 'POST':
        if request.POST.get('button')=="buttonranGuncel":
            try:
                randevuid = request.POST.get('randevuid')
                randevu = RandevuBrans.objects.get(id = randevuid)
                rdate = request.POST.get('rdate')
                rtime = request.POST.get('rtime')
                brans_id = request.POST.get('brans')
                brans = Brans.objects.get(slug = brans_id)
                doktor_id = request.POST.get('doktor')
                doktorl = Doktor.objects.get(slug = doktor_id)
            
                randevu.randevuTarih = rdate
                randevu.randevuSaat = rtime
                randevu.randevuBrans = brans
                randevu.randevuDoktor = doktorl
                randevu.save()
                return redirect('randevuListe')
            except:
                messages.warning(request, 'Böyle Randedvu Bulunmamaktadır')
                return redirect('randevuListe')
            
        if request.POST.get("button")=="buttonRandevuSil":
            randevuid = request.POST.get("randevuid")
            try:
                randevuSil = RandevuBrans.objects.get(id = randevuid)
                randevuSil.delete()
                return redirect("randevuListe")
            except:
                messages.warning(request, 'Böyle İd Bulunmamaktadır')
                return redirect('randevuListe') 

    context = {
        'randevuliste':randevuliste,
        'branslar':branslar,
        'doktorlar':doktorlar,
    }
    return render(request, 'sekreter/randevuliste.html',context)

def BransPaneli(request):
    brans = Brans.objects.all()
    if request.method == "POST":
        if request.POST.get('button') == "buttonkayit":
            brn = request.POST.get('brn')
            bransekle = Brans(ad = brn)
            bransekle.save()
            return redirect('BransPaneli')
        if request.POST.get("button")=='buttonDuyuruGuncelle':
            try:
                bransid = request.POST.get('bransid')
                bransguncel = Brans.objects.get(id = bransid)
                bransgun = request.POST.get('bransgun')
                bransguncel.ad = bransgun
                bransguncel.save()
                return redirect('BransPaneli')
            except:
                messages.warning(request, 'Böyle branş yoktor!')
        if request.POST.get("button")=="buttonBransSil":
            bransid = request.POST.get("bransid")
            try:
                bransSil = Brans.objects.get(id = bransid)
                bransSil.delete()
                return redirect("BransPaneli")
            except:
                messages.warning(request, 'Böyle İd Bulunmamaktadır')
                return redirect('BransPaneli') 
    context = {
        'brans':brans,
    }
    return render(request, 'sekreter/brans.html', context)