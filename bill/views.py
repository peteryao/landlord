from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.conf import settings

from paypal.standard.forms import PayPalPaymentsForm

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

def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        # "notify_url": "https://www.example.com" + reverse('paypal-ipn'),
        "return_url": "https://www.example.com/your-return-location/",
        "cancel_return": "https://www.example.com/your-cancel-location/",

    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "bill/payment.html", context)

def moxtra_redirect(request):
    context = {}

    return render(request, 'bill/moxtra_redirect.html', context)

def mtest(request):
    context = {}

    return render(request, 'bill/index.html', context)
