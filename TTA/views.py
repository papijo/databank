from django.shortcuts import render
from django.views import generic
from TTA.filters import TraineeFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Trainee, TradeArea, State, SpecialInterventionProgram, Centre
from TTA.forms import TraineeForm

# def index(request):

#     #Number 
#     num_trainees = Trainee.objects.all().count()
#     num_SIP = SpecialInterventionProgram.objects.all().count()
#     num_trade_areas = TradeArea.objects.all().count()

#     context = {
#         'num_trainees' : num_trainees,
#         'num_SIP' : num_SIP,
#         'num_trade_areas': num_trade_areas
#     }

#     return render(request, 'index.html', context = context)

    
@permission_required('TTA.view_trainee')
def traineeFilter(request):
    trainee_list = Trainee.objects.all()
    trainee_filter = TraineeFilter(request.GET, queryset= trainee_list)
    trainee_filter_count = trainee_filter.qs.count()


    return render(request, 'TTA/traineefilter.html', {'filter': trainee_filter, 'trainee_filter_count': trainee_filter_count})


# class TraineeListView(PermissionRequiredMixin, generic.ListView):
#     model = Trainee
#     paginate_by = 10
#     permission_required = 'TTA.view_trainee'

@permission_required('TTA.view_trainee')
def trainee_list_view(request):
    context = {}
    context['trainee_list'] = Trainee.objects.all()

    return render (request, 'TTA/trainee_list.html', context=context)

def centre_list_view(request):
    context = {}
    context['centre_list'] = Centre.objects.all()

    return render(request, 'TTA/centre_list.html', context=context)


#Trainee
class TraineeDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Trainee
    permission_required = 'TTA.view_trainee'

class TraineeCreate(PermissionRequiredMixin, CreateView):
    model = Trainee
    #fields = '__all__'
    form_class = TraineeForm
    permission_required = 'TTA.add_trainee'
   

class TraineeUpdate(PermissionRequiredMixin, UpdateView):
    model = Trainee
    fields = '__all__'
    permission_required = 'TTA.change_trainee'

class TraineeDelete(PermissionRequiredMixin, DeleteView):
    model = Trainee
    success_url = reverse_lazy('trainees')
    permission_required = 'TTA.delete_trainee'

# Centres
class CentreDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Centre
    permission_required = 'TTA.view_centre'

class CentreCreate(PermissionRequiredMixin, CreateView):
    model = Centre
    fields = '__all__'
    #form_class = CentreForm
    permission_required = 'TTA.add_centre'

class CentreUpdate(PermissionRequiredMixin, UpdateView):
    model = Centre
    fields = '__all__'
    permission_required = 'TTA.change_centre'

class CentreDelete(PermissionRequiredMixin, DeleteView):
    model = Centre
    success_url = reverse_lazy('centres')
    permission_required = 'TTA.delete_centre'

