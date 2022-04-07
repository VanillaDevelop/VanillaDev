from django.shortcuts import render
from projects.models import Project
from articles.models import Article

 #helper function for adding information the template needs to the request
def render_mainpage(request, page, vars = {}):
    #add navbar entries (depending on logged in or not)
    if(request.user.is_authenticated):
        projects = Project.objects.all().values('id', 'title', 'is_published')
        articles = Article.objects.all().values('id', 'title', 'is_published')
    else:
        projects = Project.objects.filter(is_published=True).values('id', 'title', 'is_published')
        articles = Article.objects.filter(is_published=True).values('id', 'title', 'is_published')

    vars["navbar_projects"] = projects
    vars["navbar_articles"] = articles
    return render(request, page, vars)