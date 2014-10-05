# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0004_rentbill_has_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentbill',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 13, 33, 53, 65648)),
            preserve_default=True,
        ),
    ]
