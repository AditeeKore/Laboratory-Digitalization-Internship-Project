# Generated by Django 3.2.4 on 2021-09-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0029_slot_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_Labs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_lab_name', models.CharField(max_length=20)),
                ('sub_lab_name', models.CharField(max_length=10)),
            ],
        ),
    ]