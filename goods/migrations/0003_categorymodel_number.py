# Generated by Django 2.1.1 on 2018-09-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_categorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='number',
            field=models.IntegerField(default=0, verbose_name='排序字段'),
        ),
    ]
