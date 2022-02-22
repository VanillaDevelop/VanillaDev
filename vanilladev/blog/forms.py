from django.forms import ModelForm, modelformset_factory
from .models import BlogPost, Category

CategoryFormSet = modelformset_factory(Category, extra=2, fields=['name'], can_delete=True)

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['content', 'categories', 'created_at', 'is_published']