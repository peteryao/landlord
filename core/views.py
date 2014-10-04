from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {}

    return render(request, 'core/index.html', context)
