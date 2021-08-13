from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('', views.index, name = 'index'),
    #path('organisations/', views.NasOrganisationListView.as_view(), name = 'nas-organisations'),
    path('organisations/', views.nasorganisation_listview, name = 'nas-organisations'),
    path('organisation/<int:pk>', views.NasOrganisationDetailView.as_view(), name = 'nas-organisation-detail'),
    path('organisation/create/', views.NasOrganisationCreate.as_view(), name = 'nas-organisation_create'),
    path('organisation/<int:pk>/update', views.NasOrganisationUpdate.as_view(), name = 'nas-organisation_update'),
    path('organisation/<int:pk>/delete', views.NasOrganisationDelete.as_view(), name = 'nas-organisation_delete'),
    url(r'^search/$', views.nasfilter, name='nas-search'),
]