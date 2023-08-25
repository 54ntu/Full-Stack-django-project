from django import forms
from .models import Task

class todoAppForm(forms.ModelForm):
    class Meta:
        fields = ("title","description")
        model= Task