from django import forms
from .models import Article
from datetime import date

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    created_at = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'value':date.today}))
    motivation_summary = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label="Motivation Summary")
    article_summary = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label="Article Summary")
    results_summary = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label="Results Summary")
    dataset_url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Dataset URL (Optional)", required=False)
    repository_url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Repository URL (Optional)", required=False)
    download_link_url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Download Link URL (Optional)", required=False)
    project_page_url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Project Page URL (Optional)", required=False)
    tools_csv = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Technology Stack, Comma Separated")

    class Meta:
        model = Article
        widgets = {'id': forms.HiddenInput()}
        fields = '__all__'
        labels = {
            'article_premise': 'Article Premise',
            'article_text': 'Article Text',
        }