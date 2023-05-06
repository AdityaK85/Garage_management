# Generated by Django 4.1.5 on 2023-03-21 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0015_alter_importexcel_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy_vehicle_parts',
            name='qty',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle_details',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 21, 12, 30, 19, 274719), null=True),
        ),
    ]
