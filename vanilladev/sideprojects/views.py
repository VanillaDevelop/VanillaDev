from .forms import SideProjectForm
from vanilladev.helpers import render_mainpage
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SideProject

#add side project - requires login
@login_required()
def add(request):
    #POST - save side project
    if request.method == "POST":
        form = SideProjectForm(request.POST)
        #if form is valid, redirect to overview
        if form.is_valid():
            sideproject = form.save()
            return redirect('sideprojects:overview')
        else:
            #serve the sent form again
            return render_mainpage(request, 'sideprojects/change.html', {"form":form})

    #GET - display empty sideproject page
    form = SideProjectForm()
    return render_mainpage(request, 'sideprojects/change.html', {"form":form})


#edit side project page - requires login
@login_required()
def edit(request, id):
    #POST - save sideproject
    if request.method == "POST":
        sideproject = get_object_or_404(SideProject, id=id)
        form = SideProjectForm(request.POST, instance=sideproject)
        #if form is valid, redirect to overview
        if form.is_valid():
            form.save()
            return redirect('sideprojects:overview')
        else: 
            #serve the sent form again
            return render_mainpage(request, 'sideprojects/change.html', {"form":form})

    #GET - show edit form for sideproject
    sideproject = get_object_or_404(SideProject, id=id)
    form = SideProjectForm(instance=sideproject)
    return render_mainpage(request, 'sideprojects/change.html', {"form":form})


#get home page
def index(request):
    sideprojects = SideProject.objects.all()

    #return view
    return render_mainpage(request, 'sideprojects/index.html', {"sideprojects":sideprojects})

#delete a sideproject with given id (login required)
@login_required()
def delete(request, id):
    #if post request (which passed CSRF)
    if request.method == "POST":
        #try to delete sideproject with given ID
        try:
            SideProject.objects.get(id=id).delete()
        except:
            #exceptions don't really matter here
            pass

    #redirect the user to the sideprojects overview
    return redirect('sideprojects:overview')

#sideprojects overview (login required)
@login_required()
def overview(request):
    #get all sideprojects, ordered by creation date
    sideprojects = SideProject.objects.values('id', 'title', 'project_type')
    
    return render_mainpage(request, 'sideprojects/overview.html', {"sideprojects":sideprojects})
