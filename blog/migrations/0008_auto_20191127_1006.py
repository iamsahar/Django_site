# Generated by Django 2.2.2 on 2019-11-27 10:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191127_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 27, 10, 6, 51, 275513, tzinfo=utc)),
        ),
    ]