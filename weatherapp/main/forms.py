from django.forms import ModelForm,TextInput,CharField
from .models import Weather

# Create the form class.
class CityForm(ModelForm):
   class Meta:
        model = Weather
        fields = ['city']
        widgets={'city' : TextInput(attrs={
            'placeholder':'Name of the city'
        }
        )
        }
