from typing_extensions import Required
from django.forms import ModelForm, modelformset_factory, ModelMultipleChoiceField, CheckboxSelectMultiple, HiddenInput
from .models import BlogPost, Category

CategoryFormSet = modelformset_factory(Category, extra=2, fields=['name'], can_delete=True)

class BlogPostForm(ModelForm):
    categories = ModelMultipleChoiceField(queryset=Category.objects.all(), widget=CheckboxSelectMultiple, required=True)

    class Meta:
        model = BlogPost
        widgets = {'id': HiddenInput()}
        fields = ['id', 'title', 'content', 'categories', 'created_at', 'is_published']