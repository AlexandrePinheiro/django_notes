# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 20:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='capture_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 20, 42, 12, 797445, tzinfo=utc)),
        ),
    ]
