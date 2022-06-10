from django.contrib import admin

from .models import Workstation, WorkstationRole, ContactPerson, Location

admin.site.register(Workstation)
admin.site.register(WorkstationRole)
admin.site.register(ContactPerson)
admin.site.register(Location)
