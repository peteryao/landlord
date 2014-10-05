# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0018_auto_20141005_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='debt_typedate_due',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 16, 3, 34, 213645)),
        ),
    ]
