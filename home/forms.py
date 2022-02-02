from django.forms import ModelForm, TextInput, EmailInput, Textarea
from home.models import Aloqa


class AloqaForm(ModelForm):
    class Meta:
        model = Aloqa
        fields = ['name', 'email', 'subject', 'phone', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}),
        }
