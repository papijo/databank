from TTA.models import Trainee
import django_filters

class TraineeFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr= 'icontains')
    last_name = django_filters.CharFilter(lookup_expr= 'icontains')
    other_names = django_filters.CharFilter(lookup_expr= 'icontains')
    date_of_Program =  django_filters.NumberFilter(lookup_expr='year')

    

    class Meta:
        model = Trainee
        fields = ['state', 'trade_Area', 'special_Intervention_Program']