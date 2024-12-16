from django import forms
from .models import Lab

class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ['name', 'capacity', 'resources']  # Inclua os campos desejados
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lab name'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter capacity'}),
            'resources': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter resources'}),
        }
