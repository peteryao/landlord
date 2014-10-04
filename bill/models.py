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
        return self.name