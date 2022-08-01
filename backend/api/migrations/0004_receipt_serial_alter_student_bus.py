# Generated by Django 4.0.6 on 2022-07-27 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_receipt_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='serial',
            field=models.CharField(default='U1lTjGDL', max_length=8),
        ),
        migrations.AlterField(
            model_name='student',
            name='bus',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.bus'),
        ),
    ]