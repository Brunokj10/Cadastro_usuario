# Generated by Django 4.2.2 on 2023-06-08 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usuarios',
            new_name='usuario',
        ),
    ]