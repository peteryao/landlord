import urllib2
import json
import requests

from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required

from faker import Factory
import random

from bill.models import Bill, Split_Bill
from .models import Tenant, Unit, ToDoTask

@login_required
def add_task(request):
    user = request.user
    value = request.POST['amount']
    reason = request.POST['name']
    print request.POST
    debt_typedate_due = datetime.strptime(request.POST['date_due'], '%m/%d/%Y')

    bill = Bill(user=user, value=value, reason=reason, debt_typedate_due=debt_typedate_due, is_paid=False)
    bill.save()

    tenant = Tenant.objects.get(user=request.user.id)
    unit_app = tenant.unit

    for tenant in Tenant.objects.filter(unit=unit_app):
        split = float(value) / (len(Tenant.objects.filter(unit=unit_app)) - 1)
        has_paid = False
        if tenant.user == request.user:
            has_paid = True

        final_split = Split_Bill(original=bill, user=user, split=split, has_paid=has_paid)
        final_split.save()

    return redirect('/')

@login_required
def finish_todo(request, todo_pk):
    user = request.user
    value = request.POST['amount']
    reason = request.POST['name']
    debt_typedate_due = datetime.strptime(request.POST['date_due'], '%m/%d/%Y')

    bill = Bill(user=user, value=value, reason=reason, debt_typedate_due=debt_typedate_due, is_paid=False)
    bill.save()

    tenant = Tenant.objects.get(user=request.user.id)
    unit_app = tenant.unit

    todo = ToDoTask.objects.get(pk=todo_pk)
    todo.is_complete = True
    todo.save()

    for tenant in Tenant.objects.filter(unit=unit_app):
        split = float(value) / (len(Tenant.objects.filter(unit=unit_app)) - 1)
        has_paid = False
        if tenant.user == request.user:
            has_paid = True

        final_split = Split_Bill(original=bill, user=tenant.user, split=split, has_paid=has_paid)
        print final_split
        final_split.save()

    return redirect('/')

@login_required
def venmo_bill_payment(request, bill_pk):
    bill = Split_Bill.objects.get(pk=bill_pk)
    tenant = Tenant.objects.get(user=request.user.id)
    original = bill.original
    payload = {'access_token': tenant.venmo_access_token,'email': original.user.email, 'amount': 0.01, 'note': original.reason}

    r = requests.post('https://api.venmo.com/v1/payments',data=payload)

    bill.has_paid = True
    bill.save()
    messages.add_message(request, messages.INFO, "You just paid <strong>" + original.user.email + "</strong> for " + str(bill.split) +".")
    return redirect('/')

