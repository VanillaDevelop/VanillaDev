from .forms import ArticleForm
from vanilladev.helpers import render_mainpage
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article

#add article - requires login
@login_required()
def add(request):
    #POST - save article
    if request.method == "POST":
        form = ArticleForm(request.POST)
        #if form is valid, redirect to the corresponding article
        if form.is_valid():
            article = form.save()
            return redirect('articles:page', article.id)
        else:
            #serve the sent form again
            return render_mainpage(request, 'articles/change.html', {"form":form})

    #GET - display empty article page
    form = ArticleForm()
    return render_mainpage(request, 'articles/change.html', {"form":form})


#edit article page - requires login
@login_required()
def edit(request, id):
    #POST - save article
    if request.method == "POST":
        article = get_object_or_404(Article, id=id)
        form = ArticleForm(request.POST, instance=article)
        #if form is valid, redirect to the corresponding page
        if form.is_valid():
            form.save()
            return redirect('articles:page', article.id)
        else: 
            #serve the sent form again
            return render_mainpage(request, 'articles/change.html', {"form":form})

    #GET - show edit form for article
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(instance=article)
    return render_mainpage(request, 'articles/change.html', {"form":form})


#get a article with a given ID
def page(request, id):
    #get article or 404
    article = get_object_or_404(Article, id=id)

    if not article.is_published and not request.user.is_authenticated:
        return redirect('home:index')

    #get adjacent articles or None if article is first/last
    try:
        next_article = article
        while True:
            next_article = next_article.get_next_by_created_at()
            if next_article.is_published or request.user.is_authenticated: break
    except Article.DoesNotExist:
        next_article = None

    try:
        prev_article = article
        while True:
            prev_article = prev_article.get_previous_by_created_at()
            if prev_article.is_published or request.user.is_authenticated: break
    except Article.DoesNotExist:
        prev_article = None

    #return view
    return render_mainpage(request, 'articles/article.html', {"article":article, "prev": prev_article, "next": next_article, "toolstack": article.tools_csv.split(",")})

#delete a article with given id (login required)
@login_required()
def delete(request, id):
    #if post request (which passed CSRF)
    if request.method == "POST":
        #try to delete article with given ID
        try:
            Article.objects.get(id=id).delete()
        except:
            #exceptions don't really matter here
            pass

    #redirect the user to the articles overview
    return redirect('articles:overview')

#articles overview (login required)
@login_required()
def overview(request):
    #get all articles, ordered by creation date
    articles = Article.objects.order_by('-created_at', '-id').values('id', 'created_at', 'title', 'is_published')
    
    return render_mainpage(request, 'articles/overview.html', {"articles":articles})
