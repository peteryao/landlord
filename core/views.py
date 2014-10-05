import urllib2
import json
import requests

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required

from mgmt.models import Landlord
from unit.models import Tenant, Unit
from bill.models import RentBill, Split_Bill, Bill

# Create your views here.
def index(request):
    context = {}

    # If landlord
    if Landlord.objects.filter(user=request.user.id).exists():
        return render(request, 'mgmt/index.html', context)

    # If tenant
    if Tenant.objects.filter(user=request.user.id).exists():
        context['tenant'] = Tenant.objects.get(user=request.user.id)
        return render(request, 'unit/index.html', context)

    # Not logged in
    return render(request, 'core/index.html', context)

def login_user(request):
    username = request.POST['user_name']
    password = request.POST['user_password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.add_message(request, messages.INFO, "Welcome back <strong>" + request.user.username + "</strong>!")
            return redirect(index)
        else:
            messages.add_message(request, messages.WARNING, "<strong>Error</strong>. Your account has been disabled, please contact Peter Yao.")
            return redirect(index)
    else:
        messages.add_message(request, messages.WARNING, "<strong>Error</strong>. This username/password combination is invalid. Please try again.")
        return redirect(index)

def logout_user(request):
    logout(request)
    messages.add_message(request, messages.INFO, "You have been logged out.")
    return redirect(index)

def venmo_key(request):
    tenant = Tenant.objects.get(user=request.user.id)
    tenant.venmo_access_token = request.GET['access_token']
    tenant.save()

    response = urllib2.urlopen('https://api.venmo.com/v1/me?access_token={}'.format(tenant.venmo_access_token))
    data = json.load(response)
    print data
    tenant.venmo_credit = data['data']['balance']
    tenant.venmo_photo = data['data']['user']['profile_picture_url']
    tenant.save()
    return redirect(index)

def venmo_payment(request, bill_pk):
    tenant = Tenant.objects.get(user=request.user.id)
    original = Bill.objects.get(pk=bill_pk)
    bill = Split_Bill.objects.get(original=original, user=request.user.id)
    payload = {'access_token': tenant.venmo_access_token,'email': original.user.email, 'amount': 0.01, 'note': 'First Test Run'}
    r = requests.post('https://api.venmo.com/v1/payments',data=payload)

    return redirect(index)
