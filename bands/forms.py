from django import forms
from .models import Musician  # Assuming you have a Musician model

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'other_fields_you_want_to_include']
