"""inetrecomgr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django native imports
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.static import serve

# Import from our apps
from . import views

urlpatterns = [
    url(r'^$', login_required(views.HomePage.as_view()), name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    #IP Reports views
    url(r'^ip_used_list/$', login_required(views.IPlist_Used.as_view()), name='ip_used_list'),
    url(r'^ip_decomissioned_list/$', login_required(views.IPlist_Decomissioned.as_view()), name='ip_decomissioned_list'),
    url(r'^ip_all_list/$', login_required(views.IPlist_All.as_view()), name='ip_all_list'),
    url(r'^ip_ilo_list/$', login_required(views.IPlist_ILO.as_view()), name='ip_ilo_list'),
    url(r'^ip_public_list/$', login_required(views.IPlist_Public.as_view()), name='ip_public_list'),
    url(r'^ip_servers_list/$', login_required(views.IPlist_Servers.as_view()), name='ip_servers_list'),
    url(r'^ip_netdevs_list/$', login_required(views.IPlist_Netdevs.as_view()), name='ip_netdevs_list'),
   
    #Apps views
    url(r'^netdev/', include('netdev.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^server/', include('server.urls')),
    url(r'^vserver/', include('vserver.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #Search urls
    url(r'^search/', include('haystack.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Url for file uploads
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, { 'document_root':settings.MEDIA_ROOT }),
]
