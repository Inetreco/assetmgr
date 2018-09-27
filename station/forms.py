# Django native imports
from django import forms
from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from django.utils.translation import ugettext_lazy as _

# Import from our apps
from station.models import Station

#we need to add form validation here
class StationForm(ModelForm):
    class Meta:
        model = Station
        exclude = ['created_by']

    def __init__(self, *args, **kwargs):
        super(StationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if isinstance(visible.field, forms.BooleanField):
                visible.field.widget.attrs['class'] = 'icheckbox_square-green'
            elif visible.name == "decomissioned_date":
                visible.field.widget.attrs['class'] = 'datetime-input form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

"""
if we need to add some validation here, we can do that by adding functions named clean_fieldname where fieldname is the name of the field in model.
e.g.  if we want to add antenna_type validator, we do:

from django.forms import ValidationError

    def clean_antenna_type(self):
        antenna_type = self.cleaned_data.get('antenna_type')
        if not "ANT" in antenna_type:
            raise forms.ValidationError("Your antenna type must contain characters "ANT")
        return antenna_type

We can add any logic we need here validation fields and whole forms
"""