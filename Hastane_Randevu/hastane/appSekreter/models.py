from django.db import models
from django.contrib.auth.models import *
from django.utils.text import slugify

class secreterUserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    isim = models.CharField(("İsim"), max_length=50,null=True, default="-")
    soyad = models.CharField(("Soyad"), max_length=50,null=True, default="-")
    password = models.CharField(("Şifre"), max_length=50)
    secreterTC = models.IntegerField(("TC"), default=0)
    hastaTelefon = models.CharField(("Telefon"), max_length=50, default="-")
    cinsiyet = models.CharField(("Cinsiyet"), max_length=50, default="-")


class Brans(models.Model):
    ad = models.CharField(("Branş Ad"), max_length=50)
    slug = models.SlugField(("Slug Kategori"), blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.ad)
        super(Brans, self).save(*args, **kwargs)

    def __str__(self):
        return self.ad

class Doktor(models.Model):
    isim = models.CharField(("Doktor Adı"), max_length=50, default='-')
    soyad = models.CharField(("Doktor Soyadı"), max_length=50, default='-')
    password = models.CharField(("Şifre"), max_length=50, default='-')
    doktorBrans = models.ForeignKey(Brans, verbose_name=("Doktor Branş"), on_delete=models.CASCADE, null=True, blank=True) 
    doktorTC = models.IntegerField(("Doktor TC"), default=0)
    slug = models.SlugField(("Slug Kategori"), blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super(Doktor, self).save(*args, **kwargs)
    def __str__(self):
        return self.isim + " " + self.soyad
class RandevuBrans(models.Model):
    randevuTarih = models.DateField(("Randevu Tarih"), auto_now_add=False)
    randevuSaat = models.TimeField(("Saat"), auto_now_add=False)
    randevuBrans = models.ForeignKey(Brans, verbose_name=("Randevu Branş"), on_delete=models.CASCADE)
    randevuDoktor = models.ForeignKey(Doktor, verbose_name=("Randevu Doktor"), on_delete=models.CASCADE)
    randevuDurum = models.BooleanField(("Randevu Durumu"), default=False)
    hastaTC = models.IntegerField(("Hasta TC"), default=0, null=True, blank=True)
    hastaSikayet = models.TextField(("Şikayet"), max_length=200, blank=True)


class Duyuru(models.Model):
    duyuru = models.TextField(("Duyuru"), max_length=300)

    def __str__(self):
        return self.duyuru