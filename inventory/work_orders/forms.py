from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


#


class job_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(job_form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper()
        self.helper.form_id = 'id-job_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.form_tag = False

        # You can dynamically adjust your layout
        self.helper.add_input(Submit('save', 'Save'))


    class Meta:
        model = jobs
        fields = '__all__'

class required_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(required_form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper()
        self.helper.form_id = 'id-required_form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        # You can dynamically adjust your layout
        self.helper.add_input(Submit('save', 'Save'))


    class Meta:
        model = required
        fields = '__all__'