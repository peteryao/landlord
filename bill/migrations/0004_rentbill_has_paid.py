# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0003_rentbill'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentbill',
            name='has_paid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
