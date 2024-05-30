from django import forms
from .models import Band, Musician  

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'birth']

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'musicians']
    
    musicians = forms.ModelMultipleChoiceField(
        queryset=Musician.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
