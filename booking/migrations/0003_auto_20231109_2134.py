# Generated by Django 3.2.22 on 2023-11-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20231109_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(default='00:00'),
        ),
    ]
