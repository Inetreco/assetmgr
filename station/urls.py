#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from station import views

urlpatterns = [
    url(r'^$', login_required(views.StationCreate.as_view()), name='station_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.StationUpdate.as_view()), name='station_edit'),
    url(r'^list$', login_required(views.StationList.as_view()), name='station_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.StationDelete.as_view()), name='station_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.StationDetail.as_view()), name='station_detail'),
              ]

