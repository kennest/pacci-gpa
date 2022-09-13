from django.forms import ModelForm,DateInput
from gpa_back.models import Race,Intervention
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit,Row,Column

# Create the form class.
class RaceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                "Demander une Course",
                'project',
                'applicant',
            ),
             Row(
                 Column('reason', css_class='form-group col-md-6 mb-0'),
                 Column('destination', css_class='form-group col-md-6 mb-0'),
                 css_class='form-row'
             ),
            Row(
                 Column('begin_date', css_class='form-group col-md-6 mb-0'),
                 Column('end_date', css_class='form-group col-md-6 mb-0'),
                 css_class='form-row'
             ),  
            Submit('submit', 'Soumettre', css_class='btn btn-primary'),
        )
        
    class Meta:
         model = Race
         fields = '__all__'
         exclude = ['steed','car_concerned']
         widgets = {
            'begin_date': DateInput(attrs=dict(type='date'),format='%d/%m/%Y'),
            'end_date':  DateInput(attrs=dict(type='date'),format='%d/%m/%Y'),
        }
         
# Create the form class.
class InterventionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(InterventionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                "Demander une intervention",
                'project',
                'applicant',
            ),
             Row(
                 Column('car_concerned', css_class='form-group col-md-6 mb-0'),
                 Column('destination', css_class='form-group col-md-6 mb-0'),
                 css_class='form-row'
             ),
            Row(
                 Column('date', css_class='form-group col-md-6 mb-0'),
                 Column('type', css_class='form-group col-md-6 mb-0'),
                 css_class='form-row'
             ),
            
            Submit('submit', 'Soumettre', css_class='btn btn-primary'),
        )
        
    class Meta:
         model = Intervention
         fields = '__all__'
         widgets = {
            'date': DateInput(attrs=dict(type='date'),format='%d/%m/%Y'),
        }