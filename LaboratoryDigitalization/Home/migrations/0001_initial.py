# Generated by Django 3.2.4 on 2021-08-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lab', models.CharField(max_length=20, unique=True)),
                ('NumberofPCs', models.IntegerField()),
                ('BasicConfig', models.CharField(max_length=150)),
                ('PCspurchasedinYr', models.CharField(max_length=30)),
                ('OS', models.CharField(max_length=75)),
                ('SpecialSoftware', models.CharField(max_length=100)),
            ],
        ),
    ]