# Generated by Django 4.1.5 on 2023-04-18 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appSekreter', '0004_alter_duyuru_duyuru'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appHasta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HastaRandevu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('randevuTarih', models.DateField(auto_now_add=True, verbose_name='Randevu Tarih')),
                ('randevuSaat', models.TimeField(auto_now_add=True, verbose_name='Saat')),
                ('randevuDurum', models.BooleanField(default=False, verbose_name='Randevu Durumu')),
                ('hastaTC', models.IntegerField(blank=True, default=0, null=True, verbose_name='Hasta TC')),
                ('hastaSikayet', models.TextField(blank=True, max_length=200, verbose_name='Şikayet')),
                ('randevuBrans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSekreter.brans', verbose_name='Randevu Branş')),
                ('randevuDoktor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSekreter.doktor', verbose_name='Randevu Doktor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
