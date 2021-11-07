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
    path('instructional-staff/', views.InstructionalStaffListView.as_view(), name= 'instructional-staff'),
    path('instructional-staff/<int:pk>', views.InstructionalStaffDetailView.as_view(), name= 'instructional_staff-detail'),
    path('instructional-staff/create/', views.InstructionalStaffCreate.as_view(), name = 'instructional-staff_create'),
    path('instructional-staff/<int:pk>/update', views.InstructionalStaffUpdate.as_view(), name= 'instructional-staff_update'),
    path('instructional-staff/<int:pk>/delete', views.InstructionalStaffDelete.as_view(), name= 'instructional-staff_delete'),
    path('apprentice-trainees/', views.ApprenticeTraineeListView.as_view(), name= 'apprentice-trainee'),
    path('apprentice-trainee/<int:pk>', views.ApprenticeTraineeDetailView.as_view(), name= 'apprentice_trainee-detail'),
    path('apprentice-trainee/create/', views.ApprenticeTraineeCreate.as_view(), name = 'apprentice-trainee_create'),
    path('apprentice-trainee/<int:pk>/update', views.ApprenticeTraineeUpdate.as_view(), name= 'apprentice-trainee_update'),
    path('apprentice-trainee/<int:pk>/delete', views.ApprenticeTraineeDelete.as_view(), name= 'apprentice-trainee_delete'),


    url(r'^search/$', views.nasfilter, name='nas-search'),
]