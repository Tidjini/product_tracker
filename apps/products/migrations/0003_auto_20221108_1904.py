# Generated by Django 3.2.16 on 2022-11-08 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_movement_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='valeur_actuel',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='product',
            name='valeur_initial',
        ),
    ]
