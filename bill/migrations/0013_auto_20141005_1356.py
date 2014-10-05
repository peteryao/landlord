# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0012_auto_20141005_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 13, 56, 22, 428196)),
        ),
    ]
