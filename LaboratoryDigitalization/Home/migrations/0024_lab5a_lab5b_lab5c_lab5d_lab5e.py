# Generated by Django 3.2.4 on 2021-09-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0023_lab_ready_cert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab5A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComputerName', models.CharField(max_length=20, unique=True)),
                ('Processor', models.CharField(max_length=200)),
                ('RAM', models.CharField(max_length=10)),
                ('HardDisk', models.CharField(max_length=10)),
                ('MotherBoard', models.CharField(max_length=20)),
                ('Basic_OS', models.CharField(max_length=50)),
                ('SpecialPurpose', models.CharField(max_length=150)),
                ('DateOfPurchase', models.CharField(max_length=30)),
                ('WorkingStatus', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lab5B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComputerName', models.CharField(max_length=20, unique=True)),
                ('Processor', models.CharField(max_length=200)),
                ('RAM', models.CharField(max_length=10)),
                ('HardDisk', models.CharField(max_length=10)),
                ('MotherBoard', models.CharField(max_length=20)),
                ('Basic_OS', models.CharField(max_length=50)),
                ('SpecialPurpose', models.CharField(max_length=150)),
                ('DateOfPurchase', models.CharField(max_length=30)),
                ('WorkingStatus', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lab5C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComputerName', models.CharField(max_length=20, unique=True)),
                ('Processor', models.CharField(max_length=200)),
                ('RAM', models.CharField(max_length=10)),
                ('HardDisk', models.CharField(max_length=10)),
                ('MotherBoard', models.CharField(max_length=20)),
                ('Basic_OS', models.CharField(max_length=50)),
                ('SpecialPurpose', models.CharField(max_length=150)),
                ('DateOfPurchase', models.CharField(max_length=30)),
                ('WorkingStatus', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lab5D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComputerName', models.CharField(max_length=20, unique=True)),
                ('Processor', models.CharField(max_length=200)),
                ('RAM', models.CharField(max_length=10)),
                ('HardDisk', models.CharField(max_length=10)),
                ('MotherBoard', models.CharField(max_length=20)),
                ('Basic_OS', models.CharField(max_length=50)),
                ('SpecialPurpose', models.CharField(max_length=150)),
                ('DateOfPurchase', models.CharField(max_length=30)),
                ('WorkingStatus', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lab5E',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComputerName', models.CharField(max_length=20, unique=True)),
                ('Processor', models.CharField(max_length=200)),
                ('RAM', models.CharField(max_length=10)),
                ('HardDisk', models.CharField(max_length=10)),
                ('MotherBoard', models.CharField(max_length=20)),
                ('Basic_OS', models.CharField(max_length=50)),
                ('SpecialPurpose', models.CharField(max_length=150)),
                ('DateOfPurchase', models.CharField(max_length=30)),
                ('WorkingStatus', models.CharField(max_length=30)),
            ],
        ),
    ]