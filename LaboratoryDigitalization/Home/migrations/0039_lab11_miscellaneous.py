# Generated by Django 3.2.4 on 2021-09-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0038_lab7_miscellaneous'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab11_Miscellaneous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('File', models.FileField(upload_to='uploads/lab11_miscellaneous')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
