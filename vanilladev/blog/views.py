from django.shortcuts import render
from blog.models import Category
from .forms import BlogPostForm, CategoryFormSet

def add(request):
    form = BlogPostForm()
    return render(request, 'blog/add.html', {"form":form})

def categories(request):
    formset = CategoryFormSet(queryset=Category.objects.all())
    return render(request, 'blog/categories.html', {"formset":formset})
