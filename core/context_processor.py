from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required

from mgmt.models import Landlord
from unit.models import Tenant, Unit

def landlord_units(request):
    if request.user.is_authenticated():
         if Landlord.objects.filter(user=request.user).exists():
            landlord = Landlord.objects.get(user=request.user)
            return {'units' : Unit.objects.filter(apartment=landlord.apartment)}
    return {'all_player_esports' : ()}