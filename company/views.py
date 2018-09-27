#Django native imports
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy, reverse
from django.utils.translation import ugettext as _
from django.views import generic

# Import from our apps
from company.forms import CompanyForm
from company.models import Company
from netdev.models import Netdev


class CompanyCreate(generic.CreateView):
    model = Company
    form_class = CompanyForm   
    template_name = 'company/company_form.html'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, _('Company successfully created'))
        return HttpResponseRedirect('list')


class CompanyUpdate(generic.UpdateView):
    """
    Update view for company edit page. Upon clicking "Edit" button on the
    company view page, user will be able to update a company by utilising
    this view.
    """

    model = Company
    form_class = CompanyForm
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #if not request.user.is_authenticated():
        #    return HttpResponseRedirect(reverse('login', args=(request.user.id,)))
        return super(CompanyUpdate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model
        """
        self.object = form.save()
        messages.success(self.request, _('Company successfully updated'))
        return render(self.request, 'company/company_update_form.html', {'form': form})


class CompanyList(generic.ListView):
    """
    List view for the companies
    """
    model = Company
    template_name = 'company/company_list.html'
    paginate_by = 50


class CompanyDelete(generic.DeleteView):
    model = Company
    success_url = reverse_lazy('company_list')


class CompanyDetail(generic.DetailView):
    """
    Detail view for a single company. This view is shown on the webpage 
    when user clicks on a single company in "Company list" page
    """

    model = Company
    template_name = 'company/company_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CompanyDetail, self).get(request, *args, **kwargs)