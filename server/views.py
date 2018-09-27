#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from server.forms import ServerForm
from server.models import Server


class ServerCreate(generic.CreateView):
    model = Server
    form_class = ServerForm   
    template_name = 'server/server_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Server successfully created'))
        return HttpResponseRedirect('list')


class ServerUpdate(generic.UpdateView):
    """
    Update view for server edit page. Upon clicking "Edit" button on the
    server view page, user will be able to update a server by utilising
    this view.
    """

    model = Server
    form_class = ServerForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(ServerUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('Server successfully updated'))
        return render(self.request, 'server/server_update_form.html', {'form': form})


class ServerList(generic.ListView):
    """
    List view for the servers
    """
    model = Server
    template_name = 'server/server_list.html'
    paginate_by = 50


class ServerDetail(generic.DetailView):
    """
    Detail view for a single server. This view is shown on the webpage 
    when user clicks on a single server in "Server list" page
    """

    model = Server
    template_name = 'server/server_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ServerDetail, self).get(request, *args, **kwargs)


class ServerDelete(generic.DeleteView):
    model = Server
    success_url = reverse_lazy('server_list')