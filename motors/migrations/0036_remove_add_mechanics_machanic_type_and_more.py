# Generated by Django 4.1.5 on 2023-04-03 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0035_alter_add_mechanics_machanic_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_mechanics',
            name='machanic_type',
        ),
        migrations.AlterField(
            model_name='vehicle_details',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 3, 11, 9, 18, 339660), null=True),
        ),
    ]
