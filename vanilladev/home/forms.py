from django import forms
from .models import RecentProject
from datetime import date

class RecentProjectForm(forms.ModelForm):
    class Meta:
        model = RecentProject
        widgets = {'id': forms.HiddenInput()}
        fields = '__all__'