# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0017_auto_20141005_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='date_due',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='debt_type',
        ),
        migrations.AddField(
            model_name='bill',
            name='debt_typedate_due',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 15, 51, 4, 373356)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='reason',
            field=models.CharField(default=b'Charge', max_length=256),
            preserve_default=True,
        ),
    ]
