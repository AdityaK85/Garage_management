# Generated by Django 4.1.5 on 2023-03-31 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0030_alter_vehicle_details_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_mechanics',
            name='machanic_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Machanics Type'),
        ),
        migrations.AlterField(
            model_name='vehicle_details',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 31, 15, 19, 57, 725243), null=True),
        ),
    ]
