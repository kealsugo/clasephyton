from django.contrib import admin

# Register your models here.
from .models import Roles, DatosUser, HabiUser, DetaRoles, Rates


class RolesMode(admin.ModelAdmin):
    list_display = ["RoleName"]

    class Meta:
        model = Roles

admin.site.register(Roles)

class DatosUserMode(admin.ModelAdmin):
    list_display = ["NombUser"]

    class Meta:
        model = DatosUser

admin.site.register(DatosUser)

class HabiUserMode(admin.ModelAdmin):
    list_display = ["NombHabi"]

    class Meta:
        model = HabiUser

admin.site.register(HabiUser)

class DetaRolesMode(admin.ModelAdmin):
    list_display = ["IDRole"]

    class Meta:
        model = DetaRoles

admin.site.register(DetaRoles)

class RatesMode(admin.ModelAdmin):
    list_display = ["IDHabilidades"]

    class Meta:
        model = Rates
        
admin.site.register(Rates)