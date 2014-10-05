from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required

from mgmt.models import Landlord
from unit.models import Tenant, Unit, ToDoTask
from bill.models import Split_Bill

def landlord_units(request):
    if request.user.is_authenticated():
         if Landlord.objects.filter(user=request.user.id).exists():
            landlord = Landlord.objects.get(user=request.user)
            return {'units' : Unit.objects.filter(apartment=landlord.apartment)}
    return {'failure' : ()}

def tenant_bills(request):
    if request.user.is_authenticated():
         if Tenant.objects.filter(user=request.user.id).exists():
            tenant = Tenant.objects.get(user=request.user.id)
            return {'tenant_bills' : Split_Bill.objects.filter(user=request.user.id, has_paid=False)}
    return {'failure' : ()}

def unit_todo_list(request):
    if request.user.is_authenticated():
         if Tenant.objects.filter(user=request.user.id).exists():
            tenant = Tenant.objects.get(user=request.user.id)
            return {'unit_todo_list' : ToDoTask.objects.filter(unit=tenant.unit.id, is_complete=False)}
    return {'failure' : ()}

def tenant_total(request):
    if request.user.is_authenticated():
         if Tenant.objects.filter(user=request.user.id).exists():
            tenant = Tenant.objects.get(user=request.user.id)
            print Split_Bill.objects.filter(user=1)
            return {'tenant_total' : Split_Bill.objects.filter(user=request.user.id)}
    return {'failure' : ()}

def total_tenant_transactions(request):
    if request.user.is_authenticated():
         if Tenant.objects.filter(user=request.user.id).exists():
            tenant = Tenant.objects.get(user=request.user.id)
            sum_total = 0
            for bill in Split_Bill.objects.filter(user=request.user.id, has_paid=True):
                sum_total += bill.split
            return {'total_tenant_transactions' : sum_total}
    return {'failure' : ()}