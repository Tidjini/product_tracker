# Generated by Django 3.2.16 on 2022-11-08 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movement',
            options={'ordering': ('-created_at', '-in_out', 'qte')},
        ),
    ]
