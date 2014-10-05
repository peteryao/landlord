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
    tenant_rent = []
    for tenant in Tenant.objects.filter(unit=unit_pk):
        split_bill = Split_Bill.objects.get(original=rent_bill.bill.id, user=tenant.user.id)
        tenant_rent.append(split_bill)
    context['tenant_rent'] = zip(Tenant.objects.filter(unit=unit_pk), tenant_rent)
    return render(request, 'mgmt/unit_index.html', context)

def set_rent(request, unit_pk):
    context = {}
    context['active_unit'] = Unit.objects.get(pk=unit_pk)
    context['unit_tenants'] = Tenant.objects.filter(unit=unit_pk)
    context['even_split'] = context['active_unit'].rent / len(context['unit_tenants'])
    return render(request, 'mgmt/set_rent.html', context)

def update_rent(request, unit_pk):
    context = {}
    unit = Unit.objects.get(pk=unit_pk)
    original = RentBill.objects.get(unit=unit.id, has_paid=False)
    for tenant in Tenant.objects.filter(unit=unit_pk):
        rent = request.POST['properties_' + str(tenant.id)]
        if(Split_Bill.objects.filter(original=original.id, user=request.user.id, has_paid=False).exists()):
            sBill = Split_Bill.objects.get(original=original.id, user=request.user.id, has_paid=False)
            sBill.split = rent
            sBill.save()
    return redirect(unit_index, unit_pk)