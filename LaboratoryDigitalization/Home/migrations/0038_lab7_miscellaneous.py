# Generated by Django 3.2.4 on 2021-09-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0037_lab5_miscellaneous'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab7_Miscellaneous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('File', models.FileField(upload_to='uploads/lab7a_miscellaneous')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
