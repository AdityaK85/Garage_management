# Generated by Django 4.1.5 on 2023-03-24 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0018_job_machanic_delete_buy_vehicle_parts_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='machanic_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machanic_name', models.CharField(max_length=50, verbose_name='Machanic Name')),
            ],
        ),
        migrations.RemoveField(
            model_name='job_machanic',
            name='machanic_name',
        ),
        migrations.AlterField(
            model_name='vehicle_details',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 24, 14, 45, 58, 306343), null=True),
        ),
    ]
