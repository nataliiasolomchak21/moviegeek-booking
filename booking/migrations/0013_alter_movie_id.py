# Generated by Django 3.2.22 on 2023-11-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_alter_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
