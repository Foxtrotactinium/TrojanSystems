from django import forms
from .models import *


class part_form(forms.ModelForm):
    class Meta:
        model = partslist
        fields = ('partnumber', 'description', 'location', 'supplier', 'stockonhand') #need to add other fields
