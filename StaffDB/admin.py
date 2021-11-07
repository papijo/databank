from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import StaffBio, Training, Division, Certification, Designation, State



admin.site.register(Training)



class DesignationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Designation, DesignationAdmin)

admin.site.register(Certification)

class StaffBioAdmin(admin.ModelAdmin):
    list_display = ['surname', 'firstname', 'othernames', 'staffId', 'designation', 'division', 'email_official', 'email', 'mobile_phone', 'staff_image' ]
    list_filter = ['division', 'designation']
    fields = ('surname', 'firstname', 'othernames', 'date_of_Birth', 'state_of_Origin', 'LGA', 'senatorial_District', 'sex', 'address', 'date_of_Employment', 'staffId', 'designation', 'conitfs', 'division', 'date_of_Last_Promotion', 'date_of_Next_Promotion', 'status', 'email_official', 'email', 'mobile_phone','diploma', 'bachelors_degree', 'masters_degree', 'doctorate_degree', 'certification', 'trainings_attended','image', 'favQuote','leave_Start', 'leave_End' )
    readonly_fields = ['staff_image']
    search_fields = ('surname', 'firstname', 'othernames', 'staffId',)
    
admin.site.register(StaffBio, StaffBioAdmin)


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
# @admin.register(AnnualLeave)
# class AnnualLeaveAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

