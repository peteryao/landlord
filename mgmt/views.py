from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required

from mgmt.models import Landlord
from unit.models import Tenant, Unit
from bill.models import Bill, Split_Bill, RentBill

# Create your views here.
def unit_index(request, unit_pk):
    context = {}
    unit = Unit.objects.get(pk=unit_pk)
    rent_bill = RentBill.objects.get(unit=unit, has_paid=False)
    context['split_bills'] = Split_Bill.objects.filter(original=rent_bill.bill)
    context['unit'] = unit
    context['unit_tenants'] = Tenant.objects.filter(unit=unit_pk)
    return render(request, 'mgmt/unit_index.html', context)

def set_rent(request, unit_pk):
    context = {}
    context['active_unit'] = Unit.objects.get(pk=unit_pk)
    context['unit_tenants'] = Tenant.objects.filter(unit=unit_pk)
    context['even_split'] = context['active_unit'].rent / len(context['unit_tenants'])
    return render(request, 'mgmt/set_rent.html', context)

def update_rent(request, unit_pk):
    context = {}
    return redirect(unit_index, unit_pk)