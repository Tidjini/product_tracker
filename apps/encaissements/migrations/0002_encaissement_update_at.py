# Generated by Django 3.2.16 on 2022-11-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encaissements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encaissement',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]