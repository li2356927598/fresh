# Generated by Django 2.1.1 on 2018-10-09 13:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20181009_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 21, 13, 18, 904402), verbose_name='创建时间'),
        ),
    ]
