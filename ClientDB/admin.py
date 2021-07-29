from django.contrib import admin

from django.contrib import admin

from .models import ClientOrganisation, State, Sector, AreaOffice, Type


# admin.site.register(Organisation)
# admin.site.register(State)
# admin.site.register(Sector)
# admin.site.register(area_Office)
#admin.site.register(Type)


@admin.register(ClientOrganisation)
class ClientOrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_image', 'address', 'CAC_Number', 'state', 'area_Office', 'email', 'sector', 'area_of_Specialisation', 'staff_Strength' )
    list_filter = ('sector', 'state', 'area_Office')
    fields = ('name', 'logo', 'address', 'CAC_Number', 'state', 'area_Office', 'email', 'sector', 'area_of_Specialisation', 'staff_Strength', 'date_formed')
    readonly_fields = ['logo_image']
    search_fields = ('name', 'CAC_Number')

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(AreaOffice)
class area_OfficenAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register (Type, TypeAdmin)
