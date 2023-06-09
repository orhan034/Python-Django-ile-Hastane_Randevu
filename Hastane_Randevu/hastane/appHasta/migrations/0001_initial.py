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
            name='HastaUserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(default='-', max_length=50, null=True, verbose_name='İsim')),
                ('soyad', models.CharField(default='-', max_length=50, null=True, verbose_name='Soyad')),
                ('password', models.CharField(default='-', max_length=50, null=True, verbose_name='Şifre')),
                ('hastaTC', models.IntegerField(default=0, verbose_name='TC')),
                ('hastaTelefon', models.CharField(default='-', max_length=50, verbose_name='Telefon')),
                ('cinsiyet', models.CharField(default='-', max_length=50, verbose_name='Cinsiyet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
