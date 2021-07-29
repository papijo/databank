from .models import Organisation

def Organiation_renderer(request):
    return{
        'all_organisations': Organisation.objects.all()
    }