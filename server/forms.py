# Django native imports
from django import forms
from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from django.utils.translation import ugettext_lazy as _

# Import from our apps
from server.models import Server

#we need to add form validation here
class ServerForm(ModelForm):
    class Meta:
        model = Server
        exclude = ['created_by']

    def __init__(self, *args, **kwargs):
        super(ServerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if isinstance(visible.field, forms.BooleanField):
                visible.field.widget.attrs['class'] = 'icheckbox_square-green'
            elif visible.name == "decomissioned_date":
                visible.field.widget.attrs['class'] = 'datetime-input form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-control'