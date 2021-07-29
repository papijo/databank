from django.shortcuts import render
from NasDB.models import Type, State, NasOrganisation, Sector
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .filters import OrganisationFilter, OrganisationFilterCount
from NasDB.forms import NasOrganisationForm




# def index(request):
#     # Generate counts of Organisations

#     num_nas_organisations = NasOrganisation.objects.all().count()
#     num_nas_sectors = Sector.objects.all().count()
#     num_nas_states = State.objects.all().count()

#     # Generate counts of Organisations in different apprenticeship stage
#     num_nas_organisations_promotion = NasOrganisation.objects.filter(stage__exact = 'Pr').count()
#     num_nas_organisations_appraisal = NasOrganisation.objects.filter(stage__exact = 'Ap').count()
#     num_nas_organisations_harmonisation = NasOrganisation.objects.filter(stage__exact = 'Ha').count()
#     num_nas_organisations_installation = NasOrganisation.objects.filter(stage__exact = 'In').count()
#     num_nas_organisations_supervision = NasOrganisation.objects.filter(stage__exact = 'Su').count()
#     num_nas_organisations_monitoring = NasOrganisation.objects.filter(stage__exact = 'Mo').count()

#     context = {
#         'num_nas_organisations': num_nas_organisations,
#         'num_nas_sectors': num_nas_sectors,
#         'num_nas_states': num_nas_states,
#         'num_nas_organisations_promotion': num_nas_organisations_promotion,
#         'num_nas_organisations_appraisal': num_nas_organisations_appraisal,
#         'num_nas_organisations_harmonisation': num_nas_organisations_harmonisation,
#         'num_nas_organisations_installation': num_nas_organisations_installation,
#         'num_nas_organisations_supervision': num_nas_organisations_supervision,
#         'num_nas_organisations_monitoring': num_nas_organisations_monitoring,
#     }    


#     return render(request, 'index.html', context = context)



class NasOrganisationListView(PermissionRequiredMixin, generic.ListView):
    model = NasOrganisation
    permission_required = 'NasDB.view_nasorganisation'

class NasOrganisationDetailView(PermissionRequiredMixin, generic.DetailView):
    model = NasOrganisation
    permission_required = 'NasDB.view_nasorganisation'

class NasOrganisationCreate(PermissionRequiredMixin, CreateView):
    model = NasOrganisation
    #fields = '__all__'
    form_class = NasOrganisationForm
    permission_required = 'NasDB.change_nasorganisation'
    raise_exception = False
    
    

class NasOrganisationUpdate(PermissionRequiredMixin, UpdateView):
    model = NasOrganisation
    fields = '__all__'
    permission_required = 'NasDB.change_nasorganisation'

class NasOrganisationDelete(PermissionRequiredMixin, DeleteView):
    model = NasOrganisation
    success_url = reverse_lazy('organisations')
    permission_required = 'NasDB.change_nasorganisation'


@permission_required('NasDB.view_nasorganisation')
def nasfilter(request):
    nas_organisation_list = NasOrganisation.objects.all()
    nas_organisation_filter = OrganisationFilter(request.GET, queryset=nas_organisation_list)
    nas_organisation_filter_count = nas_organisation_filter.qs.count()
    context = {
        'organisation_filter_count': nas_organisation_filter_count
        }

    
    return render(request, 'NasDB/filter.html', {'filter': nas_organisation_filter, 'nas_organisation_filter_count': nas_organisation_filter_count })