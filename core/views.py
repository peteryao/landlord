from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required

from mgmt.models import Landlord
from unit.models import Tenant, Unit

# Create your views here.
def index(request):
    context = {}
    if Landlord.objects.filter(user=request.user).exists():
        landlord = Landlord.objects.get(user=request.user)
        context['units'] = Unit.objects.filter(apartment=landlord.apartment)
        return render(request, 'mgmt/index.html', context)
    if Tenant.objects.filter(user=request.user).exists():
        pass
    return render(request, 'core/index.html', context)
