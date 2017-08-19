"""
Register your models here.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from organizations.models import (Organization, OrganizationUser, OrganizationOwner)
from .models import Account, AccountUser
from .models import Employee, Profile, Place, Driver
from .models import Program, Project, Order, OrderType, Contract, Condition
from .models import Asset, Vehicle, Inventory

# Define an inline admin descriptor for Place model
# which acts a bit like a singleton
class PlaceInline(admin.TabularInline):
    model = Place
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    inlines = (PlaceInline, )
        
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

# Define a new User admin
class CustomUserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, )
    inlines += (ProfileInline, )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',)

    list_select_related = ('profile', )
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.unregister(Organization)
admin.site.unregister(OrganizationUser)
admin.site.unregister(OrganizationOwner)

admin.site.register(Account)
admin.site.register(AccountUser)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Driver)

admin.site.register(Program)
admin.site.register(Project)
admin.site.register(Order)
admin.site.register(OrderType)
admin.site.register(Contract)
admin.site.register(Condition)

admin.site.register(Asset)
admin.site.register(Vehicle)
admin.site.register(Inventory)

admin.site.register(Place, PlaceAdmin)

from django.contrib.gis.admin import GeoModelAdmin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import WorldBorder
#admin.site.register(WorldBorder, GeoModelAdmin) # open layers
admin.site.register(WorldBorder, OSMGeoAdmin) # open street map
