# Generated by Django 3.2.4 on 2021-08-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_lab7c_lab7d_lab7e'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab7A_SW_Inst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoftwareInstalled', models.CharField(max_length=150)),
                ('Version', models.CharField(max_length=20)),
            ],
        ),
    ]
