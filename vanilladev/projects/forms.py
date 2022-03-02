from django import forms
from .models import Project
from datetime import date

class ProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    created_at = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'value':date.today}))
    motivation_summary = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    project_summary = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    dataset_url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    repository_url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    download_link_url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    project_page_url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    technology_stack_csv = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Project
        widgets = {'id': forms.HiddenInput()}
        fields = '__all__'