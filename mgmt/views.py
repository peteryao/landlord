from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required

from mgmt.models import Landlord
from unit.models import Tenant, Unit
from bill.models import Bill, Split_Bill

# Create your views here.
def unit_index(request, unit_pk):
    context = {}
    unit = Unit.objects.get(pk=unit_pk)
    context['unit'] = unit
    # bill = Bill.objects.
    context['split'] = Split_bill.objects.filter()
    return render(request, 'mgmt/unit_index.html', context)