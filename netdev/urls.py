#Django native imports
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path
from django.views.generic import edit

# Import from our apps
from netdev import views


urlpatterns = [
    url(r'^$', login_required(views.NetdevCreate.as_view()), name='netdev_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.NetdevUpdate.as_view()), name='netdev_edit'),
    url(r'^list$', login_required(views.NetdevList.as_view()), name='netdev_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.NetdevDelete.as_view()), name='netdev_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.NetdevDetail.as_view()), name='netdev_detail'),
    ]
