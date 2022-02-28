from django.shortcuts import render, redirect
from blog.models import Category
from blog.models import BlogPost
import math
from .forms import BlogPostForm, CategoryFormSet

def add(request):
    #POST - save blog post
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add')

    #GET - display new blog post
    form = BlogPostForm()
    return render(request, 'blog/change.html', {"form":form})

def edit(request, id):
    #POST - save blog post
    if request.method == "POST":
        post = BlogPost.objects.get(id=id)
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('add')

    #GET - show edit form for blog post
    post = BlogPost.objects.get(id=id)
    if post:
        form = BlogPostForm(instance=post)
        return render(request, 'blog/change.html', {"form":form})
    else:
        return redirect('home.index')


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

def post(request, id):
    #get post
    post = BlogPost.objects.get(id=id)

    if post:
        #get adjacent posts
        try:
            next_post = post.get_next_by_created_at()
        except BlogPost.DoesNotExist:
            next_post = None

        try:
            prev_post = post.get_previous_by_created_at()
        except BlogPost.DoesNotExist:
            prev_post = None

        #get categories and return
        categories = []
        for cat in post.categories.all():
            categories.append(str(cat))
        return render(request, 'blog/post.html', {"post":post, "categories": ", ".join(categories), "prev": prev_post, "next":next_post})
    else:
        #redirect
        return redirect('home.index')

def overview(request, pageno=1):
    posts = BlogPost.objects.order_by('-created_at', '-id')
    pagecount = math.ceil(posts.count()/12)
    return render(request, 'blog/overview.html', {"posts":posts[12*(pageno-1):12*(pageno)], "pagecount":pagecount, "pageno":pageno, "pages": range(1,pagecount+1)})
