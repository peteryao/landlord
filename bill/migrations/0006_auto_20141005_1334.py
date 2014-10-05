# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0005_rentbill_date_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentbill',
            name='date_due',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 13, 34, 9, 549042)),
        ),
    ]
