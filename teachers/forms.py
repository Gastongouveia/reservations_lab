from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter teacher name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter teacher email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter teacher phone'}),
        }
