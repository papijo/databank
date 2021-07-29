from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    # path('organisations/', views.ClientOrganisationListView.as_view(), name = 'client-organisations'),
    path('organisations/', views.client_list, name = 'client-organisations'),
    url(r'^organisations/sectors/(?P<sector_slug>[-\w]+)/$', views.client_list, name= 'client-organisation_by_sector'),
    url(r'^organisations/areaoffices/(?P<areaoffice_slug>[-\w]+)/$', views.client_list, name= 'client-organisation_by_areaoffice'),
    path('organisation/<int:pk>', views.ClientOrganisationDetailView.as_view(), name= 'client-organisation-detail'),
    url(r'^search/$', views.filtertest, name='client-search'),
    path('organisation/create/', views.ClientOrganisationCreate.as_view(), name = 'client-organisation_create'),
    path('organisation/<int:pk>/update', views.ClientOrganisationUpdate.as_view(), name = 'client-organisation_update'),
    path('organisation/<int:pk>/delete', views.ClientOrganisationDelete.as_view(), name = 'client-organisation_delete'),   
]
