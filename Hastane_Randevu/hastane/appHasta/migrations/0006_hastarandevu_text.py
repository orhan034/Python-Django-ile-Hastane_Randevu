# Generated by Django 4.1.5 on 2023-04-18 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHasta', '0005_rename_randevuu_hastarandevu_randevu'),
    ]

    operations = [
        migrations.AddField(
            model_name='hastarandevu',
            name='text',
            field=models.TextField(max_length=250, null=True, verbose_name='Şikayet'),
        ),
    ]
