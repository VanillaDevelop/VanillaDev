from django.shortcuts import redirect, get_object_or_404
from vanilladev.helpers import render_mainpage
from blog.models import Category
from blog.models import BlogPost
import math
from .forms import BlogPostForm, CategoryFormSet
from django.contrib.auth.decorators import login_required


#add blog post - requires login
@login_required()
def add(request):
    #POST - save blog post
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        #if form is valid, redirect to the corresponding post
        if form.is_valid():
            post = form.save()
            return redirect('blog:post', post.id)
        else:
            #serve the sent form again
            return render_mainpage(request, 'blog/change.html', {"form":form})

    #GET - display empty blog post
    form = BlogPostForm()
    return render_mainpage(request, 'blog/change.html', {"form":form})


#edit blog post - requires login
@login_required()
def edit(request, id):
    #POST - save blog post
    if request.method == "POST":
        post = get_object_or_404(BlogPost, id=id)
        form = BlogPostForm(request.POST, instance=post)
        #if form is valid, redirect to the corresponding post
        if form.is_valid():
            form.save()
            return redirect('blog:post', post.id)
        else: 
            #serve the sent form again
            return render_mainpage(request, 'blog/change.html', {"form":form})

    #GET - show edit form for blog post
    post = get_object_or_404(BlogPost, id=id)
    form = BlogPostForm(instance=post)
    return render_mainpage(request, 'blog/change.html', {"form":form})


#edit categories - requires login
@login_required()
def categories(request):
    #POST - update categories
    if request.method == "POST":
        formset = CategoryFormSet(request.POST, prefix="form", queryset=Category.objects.all())
        #save if valid, but redirect to categories either way
        if(formset.is_valid()):
            formset.save()
        return redirect('blog:categories')

    #GET - display categories
    formset = CategoryFormSet(queryset=Category.objects.all(), prefix="form")
    for form in formset.forms:
        #Set width 100 for the textboxes for category name
        form.fields["name"].widget.attrs.update({'class': 'w-100'})
    return render_mainpage(request, 'blog/categories.html', {"formset":formset})


#get a post with a given ID
def post(request, id):
    #get post or 404
    post = get_object_or_404(BlogPost, id=id)

    if not post.is_published and not request.user.is_authenticated:
        return redirect('blog:overview')

    #get adjacent posts or None if post is first/last
    try:
        next_post = post
        while True:
            next_post = next_post.get_next_by_created_at()
            if next_post.is_published or request.user.is_authenticated: break
    except BlogPost.DoesNotExist:
        next_post = None

    try:
        prev_post = post
        while True:
            prev_post = prev_post.get_previous_by_created_at()
            if prev_post.is_published or request.user.is_authenticated: break
    except BlogPost.DoesNotExist:
        prev_post = None

    #get categories of the post 
    categories = []
    for cat in post.categories.all():
        categories.append(str(cat))

    #return view
    return render_mainpage(request, 'blog/post.html', {"post":post, "categories": ", ".join(categories), "prev": prev_post, "next":next_post})

#delete a post with given id (login required)
@login_required()
def delete(request, id):
    #if post request (which passed CSRF)
    if request.method == "POST":
        #try to delete post with given ID
        try:
            BlogPost.objects.get(id=id).delete()
        except:
            #exceptions don't really matter here
            pass

    #redirect the user to the blog overview
    return redirect('blog:overview')

#blog overview
def overview(request, pageno=1):
    if request.user.is_authenticated:
        #get all posts, ordered by creation date
        posts = BlogPost.objects.order_by('-created_at', '-id')
    else:
        #only get non draft posts
        posts = BlogPost.objects.filter(is_published=True).order_by('-created_at', '-id')
    #we display 6 posts per page
    pagecount = math.ceil(posts.count()/6)
    #if the requested page number is > pagecount or < 1, opt for the last/first page
    if pageno > pagecount: return redirect('blog:overview', pagecount)
    if pageno < 1: return redirect('blog:overview', 1)
    
    return render_mainpage(request, 'blog/overview.html', {"posts":posts[6*(pageno-1):6*(pageno)], "pagecount":pagecount, "pageno":pageno, "pages": range(1,pagecount+1)})
