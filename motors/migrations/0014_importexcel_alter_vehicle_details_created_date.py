# Generated by Django 4.1.5 on 2023-03-17 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0013_alter_vehicle_details_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='importExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='import excel files')),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle_details',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 17, 12, 58, 7, 776282), null=True),
        ),
    ]
