# Generated by Django 3.2.4 on 2021-09-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0020_alter_tt_file_tt_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tt_file',
            name='tt_pdf',
            field=models.FileField(upload_to='uploads/timetable'),
        ),
    ]