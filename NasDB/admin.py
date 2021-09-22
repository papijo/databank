from django.contrib import admin
from django.db import models

from NasDB.models import NasOrganisation, Type, Sector, State, RecruitmentAndSelection, TrainingRecord, ProfessionalMembership, InstructionalStaff, ApprencticeTrainee

@admin.register(NasOrganisation)
class NasOrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_person', 'phone_number', 'email', 'state')
    list_filter = ('type', 'stage', 'provisional_approval', 'sector')
    fields = ('name', 'address', 'contact_person', 'phone_number', 'email', 'state','sector','sub_Sector', 'type', 'YOE','cac_Registration', 'cac_Reg_Number', 'itf_Registration', 'itf_Reg_Number', 'stage', 'staff_Strength_Permanent', 'staff_Strength_Temporary', 'staff_Strength_Contract', 'promotion_Officer','promotional_report_available','products', 'services','tna', 'promotional_report', 'appraisal_Officer','curriculum_available', 'curriculum_type', 'other_curriculum_type', 'recruitment_and_Selection', 'training_Approach_Practical', 'training_Approach_Theory', 'training_Approach_Otj', 'training_record_available','training_record_type', 'certification_available', 'certification_type', 'apprenticeship_Contract_Agreement', 'welfare_for_Trainees', 'appraisal_findings', 'appraisal_recommendations', 'appraisal_conclusion', 'appraisal_report_available', 'appraisal_report', 'harmonisation_Officer','types_of_Apprenticeship_Installed', 'apprencticeship_Type_Existing', 'apprenticeship_Components_Lacking', 'apprenticeship_Components_Harmonised', 'harmonisation_report_available', 'harmonisation_report', 'installation_Officer', 'apprenticeship_Type_Installed', 'apprenticeship_Components_Installed', 'installation_report_available', 'installation_report', 'ISM_Officer', 'ISM_report', 'planning_of_Training_Programme', 'proper_Use_of_Training_Facilities_tools_and_Equipment', 'use_of_Appropriate_Method_of_Training', 'record_of_Trainees_Performance', 'entries_in_Trainees_Logbook', 'adherence_to_Syllabus_and_Curriculum', 'general_Record_Keeping', 'installation_conclusion', 'ISM_report_available', 'provisional_approval', 'DOPA', 'full_approval', 'DOFA' )
    
    search_fields = ('name', 'id')


@admin.register(InstructionalStaff)
class InstructionalStaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'doe', 'organisation')
    fields = ('name', 'trade_Area', 'professional_Membership', 'doe', 'organisation')

@admin.register(ApprencticeTrainee)
class ApprenticeTrainee(admin.ModelAdmin):
    list_display = ('name', 'trade_Area', 'doe', 'organisation')
    fields = ('name', 'trade_Area', 'doe', 'organisation')

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

@admin.register(RecruitmentAndSelection)
class RecruitmentAndSelectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(TrainingRecord)
class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProfessionalMembership)
class ProfessionalMembershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}