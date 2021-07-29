from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    #path('', views.homepage, name='homepage'),
    #path('search/', views.SearchResultsView.as_view(), name = 'search_results'),
    #path('/', views.index, name = 'index'),
    path('list/', views.staff_list, name='staff'),
    #path('/search', views.SearchResultsView.as_view(), name = 'search_results'),
    # url(r'^divisions/(?P<division_slug>[-\w]+)/$', views.staff_list, name= 'staff_by_division'),
    # url(r'^designations/(?P<designation_slug>[-\w]+)/$', views.staff_list, name= 'staff_by_designation'),
    # url(r'^annualleaves/(?P<annualleave_slug>[-\w]+)/$', views.staff_list, name= 'staff_by_annualleave'),
    path('<int:pk>/', views.StaffBioDetailView.as_view(), name='staff-bio'),
    #path('/staff/<int:pk>/', views.staff_detail, name='staff-bio'),
    path('create/', views.StaffCreate.as_view(), name = 'staff_create'),
    path('<int:pk>/update/', views.StaffUpdate.as_view(), name='staff_update'),
    path('<int:pk>/delete/', views.StaffDelete.as_view(), name='staff_delete'),
    url(r'^search/$', views.staffFilter, name='staff_search'),

]