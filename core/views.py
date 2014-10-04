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
    if request.user.is_authenticated:
        if Landlord.objects.filter(user=request.user.id).exists():
            return render(request, 'mgmt/index.html', context)
        if Tenant.objects.filter(user=request.user.id).exists():
            return render(request, 'bill/index.html', context)
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