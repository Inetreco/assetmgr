#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from server import views

urlpatterns = [
    url(r'^$', login_required(views.ServerCreate.as_view()), name='server_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.ServerUpdate.as_view()), name='server_edit'),
    url(r'^list$', login_required(views.ServerList.as_view()), name='server_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.ServerDelete.as_view()), name='server_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.ServerDetail.as_view()), name='server_detail'),
              ]