from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.conf import settings

from mgmt.models import Landlord
from unit.models import Tenant, Unit
from bill.models import Bill, Split_Bill, RentBill

# Create your views here.
def unit_index(request, unit_pk):
    context = {}
    unit = Unit.objects.get(pk=unit_pk)
    context['unit'] = unit
    rent = RentBill.objects.get(unit=unit, has_paid=False)
    context['split_bill'] = Split_Bill.objects.filter(original=rent.bill)
    return render(request, 'mgmt/unit_index.html', context)

def moxtra_redirect(request):
    context = {}

    return render(request, 'bill/moxtra_redirect.html', context)

def mtest(request):
    context = {}

    return render(request, 'bill/index.html', context)


@login_required
def add_bill_item(request):
    tenant = Tenant.objects.get(user=request.user.id)
    account_name = request.POST['account_name']
    esport = request.POST['esport_value']

    player_check = Player_esport.objects.filter(player=Player.objects.get(user=request.user), esport=ESPORT.objects.get(pk=esport))

    if (player_check.count() == 0):
        player_esport = Player_esport(player=Player.objects.get(user=request.user), esport=ESPORT.objects.get(pk=esport))
        player_esport.save()
    else:
        player_esport = Player_esport.objects.get(player=Player.objects.get(user=request.user), esport=ESPORT.objects.get(pk=esport))

    player_esport_addtional = Player_esport_additional(player=player_esport, username=account_name)
    player_esport_addtional.save()
    return redirect(myesports)
