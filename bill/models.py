from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel
from unit.models import Unit

class Bill(TimeStampedModel):
    user = models.ForeignKey(User)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    debt_type = models.CharField(max_length=24, choices=(('Rent', 'Rent'), ('Utilities', 'Utilities')), default='Rent')

    def __unicode__(self):
        return "{} - {}".format(self.user.username, self.value)

class RentBill(TimeStampedModel):
    bill = models.ForeignKey(Bill)
    unit = models.ForeignKey(Unit)

    def __unicode__(self):
        return "{} - {}".format(self.unit.name, self.bill.value)

class Split_Bill(TimeStampedModel):
    original = models.ForeignKey(Bill)
    user = models.ForeignKey(User)
    split = models.DecimalField(max_digits=7, decimal_places=2)
    has_paid = models.BooleanField(default=False)

    def __unicode__(self):
        return "{} - {}".format(self.user.username, self.split)