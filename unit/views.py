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
    print bill

    return redirect('/')
