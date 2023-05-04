from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(HastaUserInfo)
class HastaUserInfoAdmin(admin.ModelAdmin):
    '''Admin View for HastaUserInfo'''

    list_display = ('user',"hastaTelefon",'hastaTC')

admin.site.register(HastaRandevu)
    
