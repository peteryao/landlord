from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User
from django.core.signals import request_finished
from django.dispatch import receiver

from core.models import TimeStampedModel
from unit.models import Unit

class Bill(TimeStampedModel):
    user = models.ForeignKey(User)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    debt_type = models.CharField(max_length=24, choices=(('Rent', 'Rent'), ('Utilities', 'Utilities')), default='Rent')
    date_due = models.DateField(default=datetime.now()+timedelta(days=7))

    def __unicode__(self):
        return "{} - {} ({})".format(self.user.username, self.value, self.debt_type)

class RentBill(TimeStampedModel):
    bill = models.ForeignKey(Bill)
    unit = models.ForeignKey(Unit)
    has_paid = models.BooleanField(default=False)
    date_due = models.DateField(default=datetime.now()+timedelta(days=7))

    def __unicode__(self):
        return "{} - {}".format(self.unit.name, self.bill.value)

class Split_Bill(TimeStampedModel):
    original = models.ForeignKey(Bill)
    user = models.ForeignKey(User)
    split = models.DecimalField(max_digits=7, decimal_places=2)
    has_paid = models.BooleanField(default=False)

    def __unicode__(self):
        return "{} - {}".format(self.user.username, self.split)