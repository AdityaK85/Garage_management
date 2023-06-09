# Generated by Django 4.1.5 on 2023-03-20 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0014_importexcel_alter_vehicle_details_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importexcel',
            name='file',
            field=models.FileField(upload_to='import_excel_files'),
        ),
        migrations.AlterField(
            model_name='vehicle_details',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 20, 12, 6, 53, 761855), null=True),
        ),
    ]
