# Generated by Django 3.2.16 on 2022-11-22 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encaissements', '0006_facturecharge_entity'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeAchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15, null=True)),
                ('entity', models.CharField(choices=[('P', 'PROMAG'), ('INF', 'INFRABITUM')], default='INF', max_length=5)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('remarque', models.CharField(max_length=255, null=True)),
                ('montant', models.DecimalField(decimal_places=3, default=0, max_digits=30)),
                ('date', models.DateField(null=True)),
                ('sender', models.CharField(max_length=15, null=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('confirm', models.BooleanField()),
                ('picture', models.FileField(blank=True, max_length=1024, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='facturecharge',
            name='montant',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=30),
        ),
    ]
