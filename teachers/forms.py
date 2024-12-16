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

class TeacherLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        try:
            teacher = Teacher.objects.get(email=email)
        except Teacher.DoesNotExist:
            raise forms.ValidationError("Invalid email or password")

        if not teacher.check_password(password):
            raise forms.ValidationError("Invalid email or password")

        self.cleaned_data["teacher"] = teacher
        return cleaned_data