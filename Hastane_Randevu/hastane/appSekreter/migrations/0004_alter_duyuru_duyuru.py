# Generated by Django 4.1.5 on 2023-04-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSekreter', '0003_duyuru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duyuru',
            name='duyuru',
            field=models.TextField(max_length=300, verbose_name='Duyuru'),
        ),
    ]