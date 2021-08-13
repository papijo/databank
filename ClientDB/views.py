from ClientDB.forms import ClientOrganisationForm
from django.shortcuts import get_object_or_404, render
from .models import ClientOrganisation, Sector, State, Type, AreaOffice
from django.views import generic
from .filters import OrganisationFilter, OrganisationFilterCount
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView, CreateView, DetailView, FormView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# @login_required
# def index(request):

#     # Number of Organisations
#     num_organisations = Organisation.objects.all().count()
#     num_sectors = Sector.objects.all().count()
#     num_areaoffices = AreaOffice.objects.all().count()

#     context = {
#         'num_organisations' : num_organisations,
#         'num_sectors': num_sectors,
#         'num_areaoffices': num_areaoffices
#     }

#     return render (request,  'main/index.html', context=context)

@permission_required('ClientDB.view_clientorganisation')
def filtertest(request):
    client_organisation_list = ClientOrganisation.objects.all()
    client_organisation_filter = OrganisationFilter(request.GET, queryset=client_organisation_list)
    client_organisation_filter_count = client_organisation_filter.qs.count()
    context = {
        'client_organisation_filter_count': client_organisation_filter_count
        }

    
    return render(request, 'ClientDB/filter.html', {'filter': client_organisation_filter, 'client_organisation_filter_count': client_organisation_filter_count })



# class ClientOrganisationListView(generic.ListView):
#     model = ClientOrganisation
#     paginate_by = 10
    

@permission_required('ClientDB.view_clientorganisation')
def client_list(request, sector_slug = None, areaoffice_slug = None, state_slug = None):
    sector = None
    sectors = Sector.objects.all()
    areaoffice = None
    areaoffices = AreaOffice.objects.all()
    state = None
    states = State.objects.all()

    client = ClientOrganisation.objects.all()

    if sector_slug:
        sector =  get_object_or_404(Sector, slug = sector_slug)
        client = ClientOrganisation.objects.filter(sector = sector)

    if state_slug:
        state =  get_object_or_404(State, slug = state_slug)
        client = ClientOrganisation.objects.filter(state = state)
    
    if areaoffice_slug:
        areaoffice =  get_object_or_404(AreaOffice, slug = areaoffice_slug)
        client = ClientOrganisation.objects.filter(areaoffice = areaoffice)

    paginator = Paginator(client, 12)
    page = request.GET.get('page')
    try:
        # create Page object for the given page
        client = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        client = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        client = paginator.page(paginator.num_pages)
    
    return render (request, 'ClientDB/clientorganisation_list.html', {
        'sector': sector,
        'sectors': sectors,
        'state': state,
        'states': states,
        'areaoffice': areaoffice,
        'areaoffices': areaoffices,
        'client': client
    })



class ClientOrganisationDetailView(PermissionRequiredMixin, generic.DetailView):
    model = ClientOrganisation
    permission_required = 'ClientDB.view_clientorganisation'



class ClientOrganisationCreate(PermissionRequiredMixin, CreateView):
    model = ClientOrganisation
    #fields = '__all__'
    form_class = ClientOrganisationForm
    permission_required = 'ClientDB.add_clientorganisation'

class ClientOrganisationUpdate(PermissionRequiredMixin, UpdateView):
    model = ClientOrganisation
    fields = '__all__'
    permission_required = 'ClientDB.change_clientorganisation'

class ClientOrganisationDelete(PermissionRequiredMixin, DeleteView):
    model = ClientOrganisation
    success_url = reverse_lazy('client-organisations')
    permission_required = 'ClientDB.delete_clientorganisation'