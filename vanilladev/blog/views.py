from django.shortcuts import render
from .forms import BlogPostForm

def add(request):
    form = BlogPostForm()
    return render(request, 'blog/add.html', {"form":form})
