from django.contrib import admin

from .models import Unit, Tenant, ToDoTask

admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(ToDoTask)