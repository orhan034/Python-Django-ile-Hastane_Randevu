from django.db import models
from django.contrib.auth.models import User
from appSekreter.models import *
# Create your models here.

class HastaUserInfo(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    isim = models.CharField(("İsim"), max_length=50,null=True, default="-")
    soyad = models.CharField(("Soyad"), max_length=50,null=True, default="-")
    password=models.CharField(("Şifre"), max_length=50, null=True, default="-")
    hastaTC = models.IntegerField(("TC"), default=0)
    hastaTelefon = models.CharField(("Telefon"), max_length=50, default="-")
    cinsiyet = models.CharField(("Cinsiyet"), max_length=50, default="-")

class HastaRandevu(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    randevu = models.ForeignKey(RandevuBrans, verbose_name=("Randevu"), on_delete=models.CASCADE, null=True)
    text = models.TextField(("Şikayet"), max_length=250, null=True)


