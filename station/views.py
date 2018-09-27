#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from station.forms import StationForm
from station.models import Station


class StationCreate(generic.CreateView):
    model = Station
    form_class = StationForm
    template_name = 'station/station_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Station successfully created'))
        return HttpResponseRedirect('list')


class StationUpdate(generic.UpdateView):
    """
    Update view for station edit page. Upon clicking "Edit" button on the
    station view page, user will be able to update a station by utilising
    this view.
    """
    model = Station
    form_class = StationForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(StationUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Station successfully updated'))
        return render(self.request, 'station/station_update_form.html', {'form': form})


class StationList(generic.ListView):
    """
    List view for the station
    """
    model = Station
    template_name = 'station/station_list.html'
    paginate_by = 25

    def get_queryset(self):
        """
        Just the queryset to feed the template
        """
        station_list = Station.objects.all().order_by("decomissioned")
        return station_list

class StationDetail(generic.DetailView):
    """
    Detail view for a single station. This view is shown on the webpage 
    when user clicks on a single station on "Station list" page
    """

    model = Station
    template_name = 'station/station_detail.html'


class StationDelete(generic.DeleteView):
    model = Station
    success_url = reverse_lazy('station_list')
