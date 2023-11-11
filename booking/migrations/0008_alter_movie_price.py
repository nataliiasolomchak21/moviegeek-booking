# Generated by Django 3.2.22 on 2023-11-11 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_movie_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='price',
            field=models.DecimalField(decimal_places=2, default='12.00', max_digits=5),
        ),
    ]