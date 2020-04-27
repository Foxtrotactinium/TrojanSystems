from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
#


class part_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(part_form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))
        # self.helper.layout = Layout(FieldWithButtons('partnumber', StrictButton("Go!")))

    class Meta:
        model = partslist
        fields = '__all__'
