#Django native imports
from django.views import generic
from django.shortcuts import render, render_to_response

# Python imports
from itertools import chain

# Import from our apps
from netdev.models import Netdev
from server.models import Server
from station.models import Station
from vserver.models import Vserver
from company.models import Company

class HomePage(generic.TemplateView):
    template_name = "fugromgr/index.html"
    context_object_name = 'context'

    def get_context_data(self,**kwargs):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        context = super().get_context_data(**kwargs)
        context['netdevs_active'] = Netdev.objects.filter(decomissioned=False)
        context['servers_active']  = Server.objects.filter(decomissioned=False)
        context['stations_active'] = Station.objects.filter(decomissioned=False)
        context['vservers_active'] = Vserver.objects.filter(decomissioned=False)
        context['companies_active'] = Company.objects.filter(inactive=False)
        context['netdevs_decomissioned'] = Netdev.objects.filter(decomissioned=True)
        context['servers_decomissioned']  = Server.objects.filter(decomissioned=True)
        context['stations_decomissioned'] = Station.objects.filter(decomissioned=True)
        context['vservers_decomissioned'] = Vserver.objects.filter(decomissioned=True)
        context['companies_decomissioned'] = Company.objects.filter(inactive=True)
        return context

"""
General view for all our apps, all reports from the navbar are under
"""

"""
IP Reports below
"""

class IPlist_Used(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/IP_used_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs in use"
        context['table_title'] = "Overview of IPs in use"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Netdev.objects.filter(decomissioned=False)
        qs2 = Server.objects.filter(decomissioned=False)
        qs3 = Station.objects.filter(decomissioned=False)
        qs4 = Vserver.objects.filter(decomissioned=False)
        ip_list = list(chain(qs1, qs2, qs3, qs4))
        return ip_list


class IPlist_Decomissioned(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/IP_decomissioned_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs Decomissioned"
        context['table_title'] = "Overview of decomissioned IPs in our infrastructure"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Netdev.objects.filter(decomissioned=True)
        qs2 = Server.objects.filter(decomissioned=True)
        qs3 = Station.objects.filter(decomissioned=True)
        qs4 = Vserver.objects.filter(decomissioned=True)
        ip_list = list(chain(qs1,qs2,qs3,qs4))
        return ip_list


class IPlist_All(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/IP_all_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs All"
        context['table_title'] = "Overview of all IPs in our infrastructure"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Netdev.objects.all().order_by("decomissioned")
        qs2 = Server.objects.all().order_by("decomissioned")
        qs3 = Station.objects.all().order_by("decomissioned")
        qs4 = Vserver.objects.all().order_by("decomissioned")
        ip_list = list(chain(qs1,qs2,qs3,qs4))
        return ip_list


class IPlist_Public(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/IP_public_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs Public"
        context['table_title'] = "Overview of used public IPs in our infrastructure"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Netdev.objects.all().order_by("decomissioned")
        qs2 = Server.objects.all().order_by("decomissioned")
        qs3 = Station.objects.all().order_by("decomissioned")
        qs4 = Vserver.objects.all().order_by("decomissioned")
        ip_list = list(chain(qs1,qs2,qs3,qs4))
        return ip_list


class IPlist_ILO(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/IP_ilo_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs iLO"
        context['table_title'] = "Overview of iLO IPs in our infrastructure"
        return context

    def get_queryset(self):
        qs1 = Server.objects.all().order_by("location")
        ip_list = qs1
        return ip_list


class IPlist_Servers(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/IP_servers_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs Servers"
        context['table_title'] = "Overview of servers IPs in our infrastructure"
        return context

    def get_queryset(self):
        """
        We have a qs per model to be queried, then is merged
        using the chain and returned to the view
        """
        qs1 = Server.objects.all().order_by("decomissioned")
        qs2 = Vserver.objects.all().order_by("decomissioned")
        ip_list = list(chain(qs1,qs2))
        return ip_list


class IPlist_Stations(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/IP_stations_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs Stations"
        context['table_title'] = "Overview of stations IPs in our infrastructure"
        return context

    def get_queryset(self):
        qs1 = Station.objects.all().order_by("decomissioned")
        ip_list = qs1
        return ip_list


class IPlist_Netdevs(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/IP_netdevs_list.html"
    context_object_name = 'ip_list'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "IPs Network Devices"
        context['table_title'] = "Overview of network devices IPs in our infrastructure"
        return context

    def get_queryset(self):
        qs1 = Netdev.objects.all().order_by("decomissioned")
        ip_list = qs1
        return ip_list

"""
End of IP Reports
"""

"""
Station reports
"""

class Stations_Sept_Receivers(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/stations_list_receivers.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        See: http://django.readthedocs.io/en/latest/topics/class-based-views/mixins.html#using-singleobjectmixin-with-listview
        This provides aditional context data without breaking the pagination.
        I tried with some other stuff(give a dict or tuple to the template with all the data), 
        but pagination wouldnt work properly or broke due TypeErrors
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Septentrio List"
        context['table_title'] = "Overview of Septentrio Receivers in our infrastructure"
        return context

    def get_queryset(self):
        """
        Just the queryset to feed the template
        """
        station_list = Station.objects.filter(receiver_brand="SEPTENTRIO").filter(decomissioned=False)
        return station_list


class Stations_Trimble_Receivers(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/stations_list_receivers.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Trimble List"
        context['table_title'] = "Overview of Trimble Receivers in our infrastructure"
        return context

    def get_queryset(self):
        """
        Queryset to feed the template
        """
        station_list = Station.objects.filter(receiver_brand="TRIMBLE").filter(decomissioned=False)
        return station_list


class Stations_Firmware(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/stations_list_firmware.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Firmware List"
        context['table_title'] = "Overview of Firmware status for receivers in our infrastructure"
        return context

    def get_queryset(self):
        """
        Queryset to feed the template
        """
        station_list = Station.objects.all().filter(decomissioned=False)
        return station_list


class Stations_Trimble_Antennas(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/stations_list_antennas.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Trimble List"
        context['table_title'] = "Overview of Trimble Antennas in our infrastructure"
        return context

    def get_queryset(self):
        """
        Queryset to feed the template
        """
        station_list = Station.objects.filter(antenna_brand="TRIMBLE").filter(decomissioned=False)
        return station_list


class Stations_Sept_Antennas(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/stations_list_antennas.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Septentrio List"
        context['table_title'] = "Overview of Septentrio Antennas in our infrastructure"
        return context

    def get_queryset(self):
        """
        Queryset to feed the template
        """
        station_list = Station.objects.filter(antenna_brand="SEPTENTRIO").filter(decomissioned=False)
        return station_list


class Stations_Radome_Antennas(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/stations_list_antennas.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Radome List"
        context['table_title'] = "Overview of Antennas with Radome in our infrastructure"
        return context

    def get_queryset(self):
        """
        Queryset to feed the template
        """
        station_list = Station.objects.filter(has_radome=True).filter(decomissioned=False)
        return station_list


class Stations_Decomissioned(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/stations_list.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Decomissioned Stations List"
        context['table_title'] = "Overview of Decomissioned Stations"
        return context

    def get_queryset(self):
        """
        Just the queryset to feed the template
        """
        station_list = Station.objects.all().filter(decomissioned=True)
        return station_list


class Stations_G4(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/stations_list.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "G4 Stations List"
        context['table_title'] = "Overview of G4 Stations"
        return context

    def get_queryset(self):
        """
        Just the queryset to feed the template
        """
        station_list = Station.objects.all().filter(decomissioned=False).filter(g4=True)
        return station_list


class Stations_GRAS(generic.ListView):
    """
    Queries all the existing objects in the DB for devices,
    Then return them as context for the view
    """
    template_name = "fugromgr/stations_list.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        """
        Feeds more context data to the template, see Stations_Sept_Receivers comments.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "GRAS Stations List"
        context['table_title'] = "Overview of GRAS Stations"
        return context

    def get_queryset(self):
        """
        Just the queryset to feed the template
        """
        station_list = Station.objects.all().filter(decomissioned=False).filter(gras=True)
        return station_list