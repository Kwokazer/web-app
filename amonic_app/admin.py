from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    pass

@admin.register(Offices)
class OfficesAdmin(admin.ModelAdmin):
    pass

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    pass