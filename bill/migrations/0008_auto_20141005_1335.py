# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0007_auto_20141005_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 13, 35, 39, 255957)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rentbill',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 13, 35, 39, 256885)),
        ),
    ]
