from .models import ClientOrganisation
import django_filters


class OrganisationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr= 'icontains')

    class Meta:
        model = ClientOrganisation
        fields = ['name', 'sector', 'area_Office', 'state']

class OrganisationFilterCount(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr= 'icontains')

    class Meta:
        model = ClientOrganisation
        fields = ['name', 'sector', 'area_Office', 'state']
