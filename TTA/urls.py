from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.index, name = 'index'),
    path('trainees/', views.TraineeListView.as_view(), name = 'trainees'),
    path('trainee/<int:pk>', views.TraineeDetailView.as_view(), name = 'trainee-detail'),
    url(r'^search/$', views.traineeFilter, name='trainee_search'),
    path('trainee/create', views.TraineeCreate.as_view(), name = 'trainee_create'),
    path('trainee/<int:pk>/update', views.TraineeUpdate.as_view(), name = 'trainee_update'),
    path('trainee/<int:pk>/delete', views.TraineeDelete.as_view(), name = 'trainee_delete'),
]
