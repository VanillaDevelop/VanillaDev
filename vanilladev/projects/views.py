from .forms import ProjectForm
from vanilladev.helpers import render_mainpage
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project

#add project - requires login
@login_required()
def add(request):
    #POST - save project
    if request.method == "POST":
        form = ProjectForm(request.POST)
        #if form is valid, redirect to the corresponding project
        if form.is_valid():
            project = form.save()
            return redirect('projects:page', project.id)
        else:
            #serve the sent form again
            return render_mainpage(request, 'projects/change.html', {"form":form})

    #GET - display empty project page
    form = ProjectForm()
    return render_mainpage(request, 'projects/change.html', {"form":form})


#edit project page - requires login
@login_required()
def edit(request, id):
    #POST - save project
    if request.method == "POST":
        project = get_object_or_404(Project, id=id)
        form = ProjectForm(request.POST, instance=project)
        #if form is valid, redirect to the corresponding page
        if form.is_valid():
            form.save()
            return redirect('projects:page', project.id)
        else: 
            #serve the sent form again
            return render_mainpage(request, 'projects/change.html', {"form":form})

    #GET - show edit form for project
    project = get_object_or_404(Project, id=id)
    form = ProjectForm(instance=project)
    return render_mainpage(request, 'projects/change.html', {"form":form})


#get a project with a given ID
def page(request, id):
    #get project or 404
    project = get_object_or_404(Project, id=id)

    if not project.is_published and not request.user.is_authenticated:
        return redirect('home:index')

    #get adjacent projects or None if project is first/last
    try:
        next_project = project
        while True:
            next_project = next_project.get_next_by_created_at()
            if next_project.is_published or request.user.is_authenticated: break
    except Project.DoesNotExist:
        next_project = None

    try:
        prev_project = project
        while True:
            prev_project = prev_project.get_previous_by_created_at()
            if prev_project.is_published or request.user.is_authenticated: break
    except Project.DoesNotExist:
        prev_project = None

    #return view
    return render_mainpage(request, 'projects/page.html', {"project":project, "prev": prev_project, "next": next_project, "techstack": project.technology_stack_csv.split(",")})

#delete a project with given id (login required)
@login_required()
def delete(request, id):
    #if post request (which passed CSRF)
    if request.method == "POST":
        #try to delete project with given ID
        try:
            Project.objects.get(id=id).delete()
        except:
            #exceptions don't really matter here
            pass

    #redirect the user to the projects overview
    return redirect('projects:overview')

#projects overview (login required)
@login_required()
def overview(request):
    #get all projects, ordered by creation date
    projects = Project.objects.order_by('-created_at', '-id').values('id', 'created_at', 'title', 'is_published')
    
    return render_mainpage(request, 'projects/overview.html', {"projects":projects})
