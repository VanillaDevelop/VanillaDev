from django import forms
from .models import BlogPost, Category
from datetime import date

CategoryFormSet = forms.modelformset_factory(Category, extra=2, fields=['name'], can_delete=True)

class BlogPostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    created_at = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'value':date.today}))

    class Meta:
        model = BlogPost
        widgets = {'id': forms.HiddenInput()}
        fields = ['id', 'title', 'content', 'categories', 'created_at', 'is_published']