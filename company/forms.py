# Django native imports
from django import forms
from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from django.utils.translation import ugettext_lazy as _

# Import from our apps
from company.models import Company

#we need to add form validation here
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = (
            'name',
            'inactive',
            'address',
            'phone',
            'contact_person',
            'email',
            )


    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == "inactive":
                visible.field.widget.attrs['class'] = 'icheckbox_square-green'
            else:
                visible.field.widget.attrs['class'] = 'form-control'