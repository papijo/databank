from django.shortcuts import render
from ClientDB.models import ClientOrganisation, Sector, State, Type, AreaOffice
from NasDB.models import NasOrganisation, Sector, State, Type
from TTA.models import Trainee, TradeArea, State, SpecialInterventionProgram
from StaffDB.models import Division, Training, StaffBio, Certification, Designation
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    #Client Organisation Information
    num_client_organisations = ClientOrganisation.objects.all().count()
    num_client_sectors = Sector.objects.all().count()
    num_client_areaoffices = AreaOffice.objects.all().count()

    #Nas Organisation Information
    num_nas_organisations = NasOrganisation.objects.all().count()
    num_nas_sectors = Sector.objects.all().count()
    num_nas_states = State.objects.all().count()

    # Generate counts of Organisations in different apprenticeship stage
    num_nas_organisations_promotion = NasOrganisation.objects.filter(stage__exact = 'Pr').count()
    num_nas_organisations_appraisal = NasOrganisation.objects.filter(stage__exact = 'Ap').count()
    num_nas_organisations_harmonisation = NasOrganisation.objects.filter(stage__exact = 'Ha').count()
    num_nas_organisations_installation = NasOrganisation.objects.filter(stage__exact = 'In').count()
    num_nas_organisations_supervision = NasOrganisation.objects.filter(stage__exact = 'Su').count()
    num_nas_organisations_monitoring = NasOrganisation.objects.filter(stage__exact = 'Mo').count()

    #Generate counts of Trainees 
    num_trainees = Trainee.objects.all().count()
    num_SIP = SpecialInterventionProgram.objects.all().count()
    num_trade_areas = TradeArea.objects.all().count()

    num_staff_on_leave = StaffBio.objects.filter(status__exact = 'Annual Leave').count()

    #Total Number of Staff
    num_staff = StaffBio.objects.all().count()
    #Total Number of Staff absconded
    num_staff_absconded = StaffBio.objects.filter(status__exact = 'Absconded').count()

    #Total Number of Staff on casual leave
    num_staff_casual_leave = StaffBio.objects.filter(status__exact = 'Casual Leave').count()

    #Total Number of Staff on sick leave
    num_staff_sick_leave = StaffBio.objects.filter(status__exact = 'Sick Leave').count()

    #Total Number of Staff on available
    num_staff_available = StaffBio.objects.filter(status__exact = 'Available').count()

    #Total Number of Staff on Career Development
    num_staff_career_development = StaffBio.objects.filter(status__exact = 'Career Development').count()

    #Total Number of Staff on Sabbatical Leave
    num_staff_sabbatical_leave = StaffBio.objects.filter(status__exact = 'Sabbatical Leave').count()

    context = {
        #Client Context
        'num_client_organisations' : num_client_organisations,
        'num_client_sectors': num_client_sectors,
        'num_client_areaoffices': num_client_areaoffices,

        #Nas Context
        'num_nas_organisations': num_nas_organisations,
        'num_nas_sectors': num_nas_sectors,
        'num_nas_states': num_nas_states,
        'num_nas_organisations_promotion': num_nas_organisations_promotion,
        'num_nas_organisations_appraisal': num_nas_organisations_appraisal,
        'num_nas_organisations_harmonisation': num_nas_organisations_harmonisation,
        'num_nas_organisations_installation': num_nas_organisations_installation,
        'num_nas_organisations_supervision': num_nas_organisations_supervision,
        'num_nas_organisations_monitoring': num_nas_organisations_monitoring,

        #Trainee Context
        'num_trainees' : num_trainees,
        'num_SIP' : num_SIP,
        'num_trade_areas': num_trade_areas,

        #Staff Database Context
        'num_staff' : num_staff,
        'num_staff_on_leave': num_staff_on_leave,
        'num_staff_absconded': num_staff_absconded,
        'num_staff_casual_leave': num_staff_casual_leave,
        'num_staff_sick_leave' : num_staff_sick_leave,
        'num_staff_available' : num_staff_available,
        'num_staff_career_development': num_staff_career_development,
        'num_staff_sabbatical_leave': num_staff_sabbatical_leave
    }


    return render (request, 'index.html', context)

