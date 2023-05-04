# Generated by Django 4.1.5 on 2023-04-16 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50, verbose_name='Branş Ad')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Doktor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(default='-', max_length=50, verbose_name='Doktor Adı')),
                ('soyad', models.CharField(default='-', max_length=50, verbose_name='Doktor Soyadı')),
                ('password', models.CharField(default='-', max_length=50, verbose_name='Şifre')),
                ('doktorTC', models.IntegerField(default=0, verbose_name='Doktor TC')),
                ('doktorBrans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appSekreter.brans', verbose_name='Doktor Branş')),
            ],
        ),
        migrations.CreateModel(
            name='secreterUserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(default='-', max_length=50, null=True, verbose_name='İsim')),
                ('soyad', models.CharField(default='-', max_length=50, null=True, verbose_name='Soyad')),
                ('password', models.CharField(max_length=50, verbose_name='Şifre')),
                ('secreterTC', models.IntegerField(default=0, verbose_name='TC')),
                ('hastaTelefon', models.CharField(default='-', max_length=50, verbose_name='Telefon')),
                ('cinsiyet', models.CharField(default='-', max_length=50, verbose_name='Cinsiyet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='RandevuBrans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('randevuTarih', models.DateField(verbose_name='Randevu Tarih')),
                ('randevuSaat', models.TimeField(verbose_name='Saat')),
                ('randevuDurum', models.BooleanField(default=False, verbose_name='Randevu Durumu')),
                ('hastaTC', models.IntegerField(blank=True, default=0, null=True, verbose_name='Hasta TC')),
                ('hastaSikayet', models.TextField(blank=True, max_length=200, verbose_name='Şikayet')),
                ('randevuBrans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSekreter.brans', verbose_name='Randevu Branş')),
                ('randevuDoktor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSekreter.doktor', verbose_name='Randevu Doktor')),
            ],
        ),
    ]
