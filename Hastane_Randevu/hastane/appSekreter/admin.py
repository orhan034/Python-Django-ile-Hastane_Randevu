from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(secreterUserInfo)
class secreterUserInfoAdmin(admin.ModelAdmin):
    '''Admin View for secreterUserInfo'''

    list_display = ('secreterTC',"password")

@admin.register(Brans)
class BransAdmin(admin.ModelAdmin):
    '''Admin View for Brans'''
    list_display = ('ad','slug')

@admin.register(Doktor)
class DoktorAdmin(admin.ModelAdmin):
    '''Admin View for Doktor'''
    list_display = ('id','isim','soyad','doktorTC','doktorBrans','password')

@admin.register(RandevuBrans)
class RandevuBransAdmin(admin.ModelAdmin):
    '''Admin View for RandevuBrans'''
    list_display = ('id','randevuTarih','randevuSaat',
                    'randevuBrans','randevuDoktor', 'randevuDurum')


@admin.register(Duyuru)
class DuyuruAdmin(admin.ModelAdmin):
    '''Admin View for Duyuru'''
    list_display = ('id','duyuru')
