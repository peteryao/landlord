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
    reason = models.CharField(max_length=256, default="Charge")
    debt_typedate_due = models.DateField(default=datetime.now()+timedelta(days=7))
    is_paid = models.BooleanField(default=False)

    def _warning_time(self):
        if datetime.now().date()+timedelta(days=7) > self.date_due:
            print "asdf"
            return True
        return False

    def _late(self):
        if datetime.now().date() > self.date_due:
            return True
        return False

    warning_time = property(_warning_time)
    late_check = property(_late)

    def __unicode__(self):
        return "{} - {} ({})".format(self.user.username, self.value, self.reason)

class RentBill(TimeStampedModel):
    bill = models.ForeignKey(Bill)
    unit = models.ForeignKey(Unit)
    has_paid = models.BooleanField(default=False)

    def __unicode__(self):
        return "{} - {}".format(self.unit.name, self.bill.value)

class Split_Bill(TimeStampedModel):
    original = models.ForeignKey(Bill)
    user = models.ForeignKey(User)
    split = models.DecimalField(max_digits=7, decimal_places=2)
    has_paid = models.BooleanField(default=False)

    def __unicode__(self):
        return "{} - {} ({})".format(self.user.username, self.split, self.has_paidhas)