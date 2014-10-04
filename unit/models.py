from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel
from mgmt.models import Apartment

class Unit(TimeStampedModel):
    name = models.CharField(max_length=10)
    rent = models.DecimalField(max_digits=7, decimal_places=2)
    apartment = models.ForeignKey(Apartment)
    venmo_access_token = models.CharField(max_length=128, default="NULL")

    def __unicode__(self):
        return self.name

class Tenant(TimeStampedModel):
    user = models.ForeignKey(User)
    unit = models.ForeignKey(Unit)

    def __unicode__(self):
        return self.user.username