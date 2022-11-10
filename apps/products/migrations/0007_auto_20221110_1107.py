# Generated by Django 3.2.16 on 2022-11-10 10:07

import django.core.files.storage
from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20221110_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qte_picture',
            field=models.FileField(blank=True, max_length=1024, null=True, storage=django.core.files.storage.FileSystemStorage(location=pathlib.PureWindowsPath('C:/Projects/product_tracker/apps/media')), upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='value_picture',
            field=models.FileField(blank=True, max_length=1024, null=True, storage=django.core.files.storage.FileSystemStorage(location=pathlib.PureWindowsPath('C:/Projects/product_tracker/apps/media')), upload_to=''),
        ),
    ]
