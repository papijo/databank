from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.index, name = 'index'),
    #path('trainees/', views.TraineeListView.as_view(), name = 'trainees'),
    path('trainees/', views.trainee_list_view, name = 'trainees'),
    path('centres/', views.centre_list_view, name = 'centres'),
    path('trainee/<int:pk>', views.TraineeDetailView.as_view(), name = 'trainee-detail'),
    path('centre/<int:pk>', views.CentreDetailView.as_view(), name = 'centre-detail'),
    url(r'^search/$', views.traineeFilter, name='trainee_search'),
    path('trainee/create', views.TraineeCreate.as_view(), name = 'trainee_create'),
    path('trainee/<int:pk>/update', views.TraineeUpdate.as_view(), name = 'trainee_update'),
    path('trainee/<int:pk>/delete', views.TraineeDelete.as_view(), name = 'trainee_delete'),
    path('centre/create', views.CentreCreate.as_view(), name = 'centre_create'),
    path('centre/<int:pk>/update', views.CentreUpdate.as_view(), name = 'centre_update'),
    path('centre/<int:pk>/delete', views.CentreDelete.as_view(), name = 'centre_delete'),
]
