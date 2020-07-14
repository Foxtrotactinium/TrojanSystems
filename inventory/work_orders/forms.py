from django import forms
from .models import Jobs, Required, ActivityLog
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
            HTML('<br>'),
            Submit('save', 'Save')
        )

    class Meta:
        model = Jobs
        fields = '__all__'


class required_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(required_form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('reqid', css_class='form-control'),
            Field('partsrequired', css_class='form-control'),
            Field('quantityrequired', css_class='form-control'),
            HTML('<br>'),
            Submit('save', 'Save')
        )

    class Meta:
        model = Required
        fields = '__all__'


class task_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(task_form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('activity_name', css_class='form-control'),
            Field('jobid', css_class='form-control'),
            # Field('partsrequired', css_class='form-control'),
            # Field('increment', css_class='form-control'),
            # Field('quantityrequired', css_class='form-control'),
            # Field('quantitycompleted', css_class='form-control'),
            # Field('timestamp', css_class='form-control'),
            # Field('user', css_class='form-control'),
            # Field('complete', css_class='form-control'),
            HTML('<br>'),
            Submit('save', 'Save')
        )

    class Meta:
        model = ActivityLog
        fields = ['activity_name', 'jobid']
