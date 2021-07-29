from django.contrib import admin

from .models import TradeArea, Trainee, State, SpecialInterventionProgram, Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

# @admin.register(Year)
# class YearAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name',)}

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
    list_display = ('trainee_image', 'last_name', 'first_name', 'other_names', 'Age', 'mobile_phone', 'email', 'address', 'Year_Of_Program', 'special_Intervention_Program', 'state', 'trade_Area', 'bank', 'account_Number', 'bvn')
    list_filter = ( 'state', 'special_Intervention_Program', 'trade_Area',)
    fields = ('image', 'last_name', 'first_name', 'other_names', 'DOB', 'mobile_phone', 'email', 'address', 'date_of_Program', 'special_Intervention_Program', 'trade_Area', 'state', 'bank', 'account_Number', 'bvn')
    search_fields = ('last_name', 'first_name', 'other_names', 'bvn',)