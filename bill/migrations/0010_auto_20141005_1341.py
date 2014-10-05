# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0009_auto_20141005_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentbill',
            name='date_due',
        ),
        migrations.AddField(
            model_name='bill',
            name='is_paid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 13, 41, 0, 815161)),
        ),
    ]
