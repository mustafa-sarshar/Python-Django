# Generated by Django 3.1.3 on 2022-01-16 16:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_data',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 16, 7, 3, 751491, tzinfo=utc)),
        ),
    ]
