# Generated by Django 4.1.5 on 2023-02-28 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0012_alter_vehicle_details_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_details',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 28, 15, 47, 16, 439358), null=True),
        ),
    ]
