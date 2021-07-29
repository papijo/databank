from django.contrib import admin
from django.db import models

from NasDB.models import NasOrganisation, Type, Sector, State

@admin.register(NasOrganisation)
class NasOrganisationAdmin(admin.ModelAdmin):
    list_display = ('name','address', 'state', 'id', 'type', 'stage', 'sector', 'YOE', 'staff_Strength',  'area_of_Specialization', 'promotion_Officer', 'appraisal_Officer', 'harmonisation_Officer', 'installation_Officer', 'supervision_Officer', 'monitoring_Officer', 'provisional_approval', 'DOPA' )
    list_filter = ('type', 'stage', 'provisional_approval', 'sector')
    fields = ('name', 'address', 'state', 'type', 'YOE', 'stage', 'sector', 'staff_Strength', 'area_of_Specialization', 'promotion_Officer', 'appraisal_Officer', 'harmonisation_Officer', 'installation_Officer', 'supervision_Officer', 'monitoring_Officer', 'provisional_approval', 'DOPA' )
    search_fields = ('name', 'id')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register (Type, TypeAdmin)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}