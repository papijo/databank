from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic
from StaffDB.models import Division, Training, StaffBio, Certification, Designation
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView
from django.db.models import Q
from .forms import StaffBioForm
from .filters import StaffbioFilter





# def homepage(request):


#     return render(request, 'homepage.html')

# @login_required 
# def index(request):
#     #Total Number of Staff
#     num_staff = StaffBio.objects.all().count()

#     #Total Number of Staff on leave
#     num_staff_on_leave = AnnualLeaveStatus.objects.filter(status__exact = 'l').count()

#     #Total Number of Staff absconded
#     num_staff_absconded = AnnualLeaveStatus.objects.filter(status__exact = 'ab').count()

#     #Total Number of Staff on casual leave
#     num_staff_casual_leave = AnnualLeaveStatus.objects.filter(status__exact = 'c').count()

#     #Total Number of Staff on sick leave
#     num_staff_sick_leave = AnnualLeaveStatus.objects.filter(status__exact = 'sl').count()

#     #Total Number of Staff on available
#     num_staff_available = AnnualLeaveStatus.objects.filter(status__exact = 'av').count()

#     #Total Number of Staff on Career Development
#     num_staff_career_development = AnnualLeaveStatus.objects.filter(status__exact = 'ca').count()

#     #Total Number of Staff on Sabbatical Leave
#     num_staff_sabbatical_leave = AnnualLeaveStatus.objects.filter(status__exact = 'sb').count()
#     context = {
#         'num_staff' : num_staff,
#         'num_staff_on_leave': num_staff_on_leave,
#         'num_staff_absconded': num_staff_absconded,
#         'num_staff_casual_leave': num_staff_casual_leave,
#         'num_staff_sick_leave' : num_staff_sick_leave,
#         'num_staff_available' : num_staff_available,
#         'num_staff_career_development': num_staff_career_development,
#         'num_staff_sabbatical_leave': num_staff_sabbatical_leave
#     }

#     return render(request, 'index.html', context = context)

#@login_required
@permission_required('StaffDB.view_staffbio')  
def staff_list(request, division_slug = None, designation_slug = None):
    division = None
    divisions = Division.objects.all()
    designation = None
    designations = Designation.objects.all()

    staff = StaffBio.objects.all()

    if division_slug:
        division = get_object_or_404(Division, slug = division_slug)
        staff = StaffBio.objects.filter(division = division)
    
    if designation_slug:
        designation = get_object_or_404(Designation, slug = designation_slug)
        staff =  StaffBio.objects.filter(designation = designation)
    
    # if annualleave_slug:
    #     annualleave = get_object_or_404(AnnualLeave, slug = annualleave_slug)
    #     staff = StaffBio.objects.filter(annualleave = annualleave)
    
    paginator = Paginator(staff, 12)
    page = request.GET.get('page')
    try:
        # create Page object for the given page
        staff = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        staff = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        staff = paginator.page(paginator.num_pages)
    
    

    return render (request, 'StaffDB/staffbio_list.html', {
        'division': division,
        'divisions': divisions,
        'designation': designation,
        'designations': designations,
        # 'annualleave': annualleave,
        # 'annualleaves': annualleaves,
        'staff': staff
        
    })


# def staff_detail(request, staffId = pk):

#     try:
#         staffBio = StaffBio.objects.get(staffId = staffId)
#     except StaffBio.DoesNotExist:
#         raise Http404('Staff does not exist')
    
#     return render(request, 'staffinfo/staffbio_detail.html', context={'staffBio': staffBio})


class StaffBioDetailView(PermissionRequiredMixin, generic.DetailView):
    model = StaffBio
    permission_required = 'StaffDB.view_staffbio'

class StaffCreate(PermissionRequiredMixin, CreateView):
    model = StaffBio
    form_class = StaffBioForm
    #fields = '__all__'
    #permission_required = 'staffbio.can_edit'
    permission_required = 'StaffDB.add_staffbio'
    
class StaffUpdate(PermissionRequiredMixin, UpdateView):
    model = StaffBio
    fields = '__all__'
    #permission_required = 'staffbio.can_edit'
    permission_required = 'StaffDB.change_staffbio'
    

class StaffDelete(PermissionRequiredMixin, DeleteView):
    model = StaffBio
    success_url = reverse_lazy('staff')
    permission_required = 'StaffDB.delete_staffbio'
    template_name = 'StaffDB/staffbio_confirm_delete.html'
    #permission_required = 'staffbio.can_edit'


# class SearchResultsView(LoginRequiredMixin, generic.ListView):
#     model = StaffBio
#     template_name = 'staffinfo/search_results.html'

#     def get_queryset(self):
#         query = self.request.GET.get('staffSearch')
#         object_list = StaffBio.objects.filter(Q(surname__icontains = query) |Q(firstname__icontains = query) | Q(staffId__icontains = query))
#         return object_list

@permission_required('StaffDB.view_staffbio')
def staffFilter(request):
    staff_list = StaffBio.objects.all()
    staff_filter =  StaffbioFilter(request.GET, queryset= staff_list)
    staff_filter_count = staff_filter.qs.count()


    return render(request, 'StaffDB/filter.html', {'filter': staff_filter, 'staff_filter_count': staff_filter_count})