from attr import attrs
from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from TodoApp.models import Todo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class Todoform(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'status', 'priority' ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),    
        }

        
            