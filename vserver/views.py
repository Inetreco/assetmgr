#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from vserver.forms import VserverForm
from vserver.models import Vserver


class VserverCreate(generic.CreateView):
    model = Vserver
    form_class = VserverForm   
    template_name = 'vserver/vserver_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('vServer successfully created'))
        return HttpResponseRedirect('list')


class VserverUpdate(generic.UpdateView):
    """
    Update view for vServer edit page. Upon clicking "Edit" button on the
    server view page, user will be able to update a vServer by utilising
    this view.
    """

    model = Vserver
    form_class = VserverForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(VserverUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        obj = form.save(commit=False)
        obj.created_by = self.request.user.username
        obj.save()
        messages.success(self.request, _('vServer successfully updated'))
        return render(self.request, 'vserver/vserver_update_form.html', {'form': form})


class VserverList(generic.ListView):
    """
    List view for the servers
    """
    model = Vserver
    template_name = 'vserver/vserver_list.html'
    paginate_by = 50


class VserverDetail(generic.DetailView):
    """
    Detail view for a single vserver. This view is shown on the webpage 
    when user clicks on a single server in "vServer list" page
    """

    model = Vserver
    template_name = 'vserver/vserver_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(VserverDetail, self).get(request, *args, **kwargs)


class VserverDelete(generic.DeleteView):
    model = Vserver
    success_url = reverse_lazy('vserver_list')