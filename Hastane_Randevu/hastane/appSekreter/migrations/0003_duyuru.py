# Generated by Django 4.1.5 on 2023-04-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSekreter', '0002_doktor_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duyuru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duyuru', models.CharField(max_length=50, verbose_name='Duyuru')),
            ],
        ),
    ]
