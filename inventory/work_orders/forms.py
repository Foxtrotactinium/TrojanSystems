from django import forms
from .models import jobs, required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class job_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(job_form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('jobid', css_class='form-control'),
            Field('description', css_class='form-control'),
            Submit('save', 'Save')
        )

    class Meta:
        model = jobs
        fields = '__all__'

class required_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        jobid = kwargs.pop('reqid')
        super(required_form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.fields['reqid'].initial = jobid
        self.helper.layout = Layout(
            Field('reqid', jobid.id, css_class='form-control'),
            Field('partsrequired', css_class='form-control', rows="2"),
            Field('quantityrequired', css_class='form-control'),
            Field('increment'),
            HTML('<br>'),
            Submit('save', 'Add Part')
        )

    class Meta:
        model = required
        fields = '__all__'