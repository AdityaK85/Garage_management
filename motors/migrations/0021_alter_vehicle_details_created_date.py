# Generated by Django 4.1.5 on 2023-03-24 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0020_job_order_alter_vehicle_details_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_details',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 24, 15, 52, 6, 848002), null=True),
        ),
    ]
