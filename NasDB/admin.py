from django.contrib import admin
from django.db import models

from NasDB.models import NasOrganisation, Type, Sector, State

@admin.register(NasOrganisation)
class NasOrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_person', 'phone_number', 'email', 'state', 'type', 'YOE', 'stage', 'sector', 'staff_Strength', 'area_of_Specialization', 'promotion_Officer','promotional_report_available', 'appraisal_Officer','curriculum_available', 'curriculum_type','training_record_available','training_record_type', 'certification_available', 'certification_type', 'appraisal_report_available', 'harmonisation_Officer', 'harmonisation_report_available', 'installation_Officer', 'installation_report_available', 'supervision_Officer', 'supervision_report_available', 'monitoring_Officer', 'monitoring_report_available', 'provisional_approval', 'DOPA' )
    list_filter = ('type', 'stage', 'provisional_approval', 'sector')
    fields = ('name', 'address', 'contact_person', 'phone_number', 'email', 'state', 'type', 'YOE', 'stage', 'sector', 'staff_Strength', 'area_of_Specialization', 'promotion_Officer','promotional_report_available', 'appraisal_Officer','curriculum_available', 'curriculum_type','training_record_available','training_record_type', 'certification_available', 'certification_type', 'appraisal_report_available', 'harmonisation_Officer', 'harmonisation_report_available', 'installation_Officer', 'installation_report_available', 'supervision_Officer', 'supervision_report_available', 'monitoring_Officer', 'monitoring_report_available', 'provisional_approval', 'DOPA' )
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