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
