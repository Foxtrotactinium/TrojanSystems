from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
#
# register = template.library()
#
# @register.filter(name='detailcss')

class part_form(forms.ModelForm):
    class Meta:
        model = partslist
        labels = {
                'partnumber':('Part Number'),
                'stockonhand':('Stock on Hand'),
                'minimumstock':('Minimum Stock'),
                'reorderqtys':('Reorder Quantities')
        }
        fields = ('partnumber', 'description', 'location', 'supplier', 'stockonhand', 'minimumstock', 'reorderqtys')

        helper = FormHelper()
        helper.form_class = 'form-horizontal'
        helper.layout = Layout(
            Field('text_input', style='background: #FAFAFA'),
            Field('textarea', rows="3", css_class='input-xlarge'),
            'radio_buttons',
            Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
            AppendedText('appended_text', '.00'),
            PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">',
                          active=True),
            PrependedText('prepended_text_two', '@'),
            'multicolon_select',
            FormActions(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
                Submit('cancel', 'Cancel'),
            )
        )