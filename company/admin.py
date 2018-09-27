from django.contrib import admin
from server.models import Server
from company.models import Company
from netdev.models import Netdev
from vserver.models import Vserver

admin.site.register(Server)
admin.site.register(Company)
admin.site.register(Netdev)
admin.site.register(Vserver)