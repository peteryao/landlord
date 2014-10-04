# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0006_unit_apartment'),
        ('bill', '0002_split_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentBill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('bill', models.ForeignKey(to='bill.Bill')),
                ('unit', models.ForeignKey(to='unit.Unit')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
