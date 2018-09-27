# Django native imports
from django import forms
from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from django.utils.translation import ugettext_lazy as _

# Import from our apps
from netdev.models import Netdev

# we need to add form validation here
class NetdevForm(ModelForm):
    class Meta:
        model = Netdev
        exclude = ['created_by']

    def __init__(self, *args, **kwargs):
        super(NetdevForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if isinstance(visible.field, forms.BooleanField):
                visible.field.widget.attrs['class'] = 'icheckbox_square-green'
            elif visible.name == "decomissioned_date":
                visible.field.widget.attrs['class'] = 'datetime-input form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
