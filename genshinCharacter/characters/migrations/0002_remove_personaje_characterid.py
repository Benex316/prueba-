# Generated by Django 4.1.3 on 2022-11-15 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaje',
            name='characterID',
        ),
    ]