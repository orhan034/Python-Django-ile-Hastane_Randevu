# Generated by Django 4.1.5 on 2023-04-18 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appHasta', '0003_remove_hastarandevu_hastasikayet_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hastarandevu',
            old_name='randevu',
            new_name='randevuu',
        ),
    ]
