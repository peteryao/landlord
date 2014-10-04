# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0003_auto_20141004_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='apartment',
            field=models.ForeignKey(default=0, to='mgmt.Apartment'),
        ),
    ]
