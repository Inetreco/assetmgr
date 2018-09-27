#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from vserver import views

urlpatterns = [
    url(r'^$', login_required(views.VserverCreate.as_view()), name='vserver_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.VserverUpdate.as_view()), name='vserver_edit'),
    url(r'^list$', login_required(views.VserverList.as_view()), name='vserver_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.VserverDelete.as_view()), name='vserver_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.VserverDetail.as_view()), name='vserver_detail'),
              ]