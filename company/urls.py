#Django native imports
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import edit

# Import from our apps
from company import views

urlpatterns = [
    url(r'^$', login_required(views.CompanyCreate.as_view()), name='company_create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.CompanyUpdate.as_view()), name='company_edit'),
    url(r'^list$', login_required(views.CompanyList.as_view()), name='company_list'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.CompanyDelete.as_view()), name='company_delete'),
    url(r'^(?P<pk>\d+)/$', login_required(views.CompanyDetail.as_view()), name='company_detail'),
              ]