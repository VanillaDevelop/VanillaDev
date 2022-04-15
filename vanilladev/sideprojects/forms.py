from django import forms
from .models import SideProject

class SideProjectForm(forms.ModelForm):
    class Meta:
        model = SideProject
        widgets = {'id': forms.HiddenInput()}
        fields = '__all__'