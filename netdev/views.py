#Django native imports
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _

# Import from our apps
from netdev.forms import NetdevForm
from netdev.models import Netdev

class NetdevCreate(generic.CreateView):
    model = Netdev
    form_class = NetdevForm
    template_name = 'netdev/netdev_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Network device successfully created'))
        return HttpResponseRedirect('list')


class NetdevUpdate(generic.UpdateView):
    """
    Update view for netdev edit page. Upon clicking "Edit" button on the
    netdev view page, user will be able to update a netdev by utilising
    this view.
    """

    model = Netdev
    form_class = NetdevForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(NetdevUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Network device has been successfully updated'))
        return render(self.request, 'netdev/netdev_update_form.html', {'form': form})


class NetdevList(generic.ListView):
    """
    List view for the network devices
    """
    model = Netdev
    template_name = 'netdev/netdev_list.html'
    paginate_by = 50


class NetdevDelete(generic.DeleteView):
    model = Netdev
    success_url = reverse_lazy('netdev_list')


class NetdevDetail(generic.DetailView):
    """
    Detail view for a single network device. This view is shown on the webpage
    when user clicks on a single network device on "Netdev list" page
    """

    model = Netdev
    template_name = 'netdev/netdev_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(NetdevDetail, self).get(request, *args, **kwargs)