from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel

class Apartment(TimeStampedModel):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Landlord(TimeStampedModel):
    apartment = models.ForeignKey(Apartment)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "{} - {}".format(self.user.username, self.apartment)