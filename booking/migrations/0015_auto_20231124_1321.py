# Generated by Django 3.2.22 on 2023-11-24 13:21

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_auto_20231124_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(choices=[('2024-01-24', 'January 24, 2024'), ('2024-01-26', 'January 26, 2024'), ('2024-01-30', 'January 30, 2024')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[('12:00', '12:00 PM'), ('15:00', '3:00 PM'), ('19:00', '7:00 PM')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
