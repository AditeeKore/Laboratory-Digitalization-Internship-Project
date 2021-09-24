# Generated by Django 3.2.4 on 2021-09-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0026_lab5b_sw_inst_lab5c_sw_inst_lab5d_sw_inst_lab5e_sw_inst'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab11A',
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
            name='Lab11A_SW_Inst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoftwareInstalled', models.CharField(max_length=50)),
                ('Version', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lab11B',
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
            name='Lab11B_SW_Inst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoftwareInstalled', models.CharField(max_length=50)),
                ('Version', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]