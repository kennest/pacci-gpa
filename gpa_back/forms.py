from django.forms import ModelForm
from gpa_back.models import Race,Intervention

# Create the form class.
class RaceForm(ModelForm):
    class Meta:
         model = Race
         fields = '__all__'
         exclude = ['steed','car_concerned']