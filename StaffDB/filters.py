from .models import StaffBio
import django_filters

class StaffbioFilter(django_filters.FilterSet):
    surname = django_filters.CharFilter(lookup_expr='icontains')
    firstname = django_filters.CharFilter(lookup_expr='icontains')
    othernames  = django_filters.CharFilter(lookup_expr= 'icontains')
    staffId = django_filters.NumberFilter(lookup_expr='icontains')
    

    class Meta:
        model = StaffBio
        fields = ['designation', 'division', 'trainings_attended']