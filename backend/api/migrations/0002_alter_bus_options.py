# Generated by Django 4.0.6 on 2022-07-27 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bus',
            options={'managed': True, 'verbose_name': 'Bus', 'verbose_name_plural': 'Buses'},
        ),
    ]
