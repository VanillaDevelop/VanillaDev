from django.shortcuts import render, redirect
from blog.models import Category
from .forms import BlogPostForm, CategoryFormSet

def add(request):
    form = BlogPostForm()
    return render(request, 'blog/change.html', {"form":form})

def categories(request):
    #POST - update categories
    if request.method == "POST":
        formset = CategoryFormSet(request.POST, prefix="form", queryset=Category.objects.all())
        if(formset.is_valid()):
            formset.save()
        return redirect('categories')

    else:
        #GET - display categories
        formset = CategoryFormSet(queryset=Category.objects.all(), prefix="form")
        for form in formset.forms:
            #Set width 100 for the textboxes for category name
            form.fields["name"].widget.attrs.update({'class': 'w-100'})
        return render(request, 'blog/categories.html', {"formset":formset})
