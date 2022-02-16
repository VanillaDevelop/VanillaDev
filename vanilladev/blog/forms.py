from django.forms import ModelForm, modelformset_factory
from .models import BlogPost, Category

CategoryFormSet = modelformset_factory(Category, extra=2, fields=['name'])

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['content', 'categories']