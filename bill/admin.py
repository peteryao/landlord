from django.contrib import admin

from .models import Bill, Split_Bill, RentBill

admin.site.register(Bill)
admin.site.register(Split_Bill)
admin.site.register(RentBill)