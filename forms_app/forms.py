from .models import FormModel2
from django import forms

class EntryForm(forms.ModelForm):
    class Meta:
        model= FormModel2
        fields = '__all__'