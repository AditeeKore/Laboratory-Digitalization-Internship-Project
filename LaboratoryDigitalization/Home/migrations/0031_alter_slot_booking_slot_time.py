# Generated by Django 3.2.4 on 2021-09-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0030_booking_labs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot_booking',
            name='slot_time',
            field=models.CharField(max_length=100),
        ),
    ]
