# Generated by Django 2.0.13 on 2019-05-14 19:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('managerLibrary', '0002_auto_20190514_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 19, 9, 24, 490526, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='presence',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 19, 9, 24, 493445, tzinfo=utc)),
        ),
    ]
