# Generated by Django 4.1.5 on 2023-04-18 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appSekreter', '0004_alter_duyuru_duyuru'),
        ('appHasta', '0007_remove_hastarandevu_randevu_hastarandevu_randevu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hastarandevu',
            name='randevu',
        ),
        migrations.AddField(
            model_name='hastarandevu',
            name='randevu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appSekreter.randevubrans', verbose_name='Randevu'),
        ),
    ]
