from django.contrib import admin

from .models import TradeArea, Trainee, State, SpecialInterventionProgram, Bank, Centre


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Centre)
class CentreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','state', 'display_trade_area', 'contact_Person', 'contact_Phone_Number', 'bank', 'account_Number')
    fields = ('name', 'address', 'state', 'trade_Area', 'contact_Person', 'contact_Phone_Number', 'bank', 'account_Number')
    search_fields = ('name', 'contact_Phone_Number')
    

@admin.register(TradeArea)
class TradeAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SpecialInterventionProgram)
class SpecialInterventionProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ('trainee_image', 'last_name', 'first_name', 'other_names', 'Age', 'mobile_phone','centre','email', 'address', 'Year_Of_Program', 'special_Intervention_Program', 'state', 'trade_Area', 'bank', 'account_Number', 'bvn')
    list_filter = ( 'state', 'special_Intervention_Program', 'trade_Area', 'centre')
    fields = ('image', 'last_name', 'first_name', 'other_names', 'DOB', 'mobile_phone', 'email', 'address', 'date_of_Program', 'special_Intervention_Program','centre', 'trade_Area', 'state', 'bank', 'account_Number', 'bvn')
    search_fields = ('last_name', 'first_name', 'other_names', 'bvn',)