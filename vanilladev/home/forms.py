from django import forms
from .models import RecentProject

class RecentProjectForm(forms.ModelForm):
    class Meta:
        model = RecentProject
        fields = "__all__"

