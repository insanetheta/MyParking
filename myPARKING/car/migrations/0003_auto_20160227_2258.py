# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 06:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20160227_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 22, 58, 21, 910000), editable=False, verbose_name=b'created'),
        ),
        migrations.AlterField(
            model_name='car',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 27, 22, 58, 21, 910000), verbose_name=b'modified'),
        ),
    ]
