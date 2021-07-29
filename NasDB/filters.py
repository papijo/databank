from NasDB.models import NasOrganisation
import django_filters


class OrganisationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr= 'icontains')

    class Meta:
        model = NasOrganisation
        fields = ['name', 'sector', 'state']

class OrganisationFilterCount(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr= 'icontains')

    class Meta:
        model = NasOrganisation
        fields = ['name', 'sector', 'state']
