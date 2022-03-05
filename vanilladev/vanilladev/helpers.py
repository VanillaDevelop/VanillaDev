from django.shortcuts import render
from projects.models import Project

 #helper function for adding information the template needs to the request
def render_mainpage(request, page, vars = {}):
    #add all public projects for the navbar
    projects = Project.objects.filter(is_published=True).values('id', 'title')
    vars["navbar_projects"] = projects
    return render(request, page, vars)