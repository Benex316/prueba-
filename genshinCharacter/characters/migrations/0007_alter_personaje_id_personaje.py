# Generated by Django 4.1.3 on 2022-12-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_alter_personaje_id_personaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaje',
            name='id_personaje',
            field=models.AutoField(db_column='id_personaje', primary_key=True, serialize=False),
        ),
    ]
