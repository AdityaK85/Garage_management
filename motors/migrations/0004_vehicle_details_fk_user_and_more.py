# Generated by Django 4.1.5 on 2023-02-21 06:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0003_alter_vehicle_details_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_details',
            name='fk_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='motors.add_new_cust', verbose_name='Vehicle Holding Name'),
        ),
        migrations.AddField(
            model_name='vehicle_details',
            name='veh_cust_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle_details',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.date(2023, 2, 21), null=True),
        ),
    ]
