from django import forms
from django.forms.models import ModelForm
from .models import URL

class CreateForm(ModelForm):
    class Meta:
        model = URL
        fields = ['url']
