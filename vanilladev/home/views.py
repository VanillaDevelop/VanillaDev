from django.shortcuts import redirect
from vanilladev.helpers import render_mainpage
from django.contrib.auth.decorators import login_required
from .forms import RecentProjectForm
from .models import RecentProject

# Create your views here.
def index(request):
    recents = list(reversed(RecentProject.objects.all()))[:4]
    return render_mainpage(request, 'home/index.html', {'recents': recents})

#change recent projects
@login_required()
def recentprojects(request, id=None):
    #if this is a post request, store the posted recent project
    if request.method == 'POST' and id is not None:
        form = RecentProjectForm(request.POST, instance=RecentProject.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('home:recentprojects')
    elif request.method == 'POST':
        form = RecentProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:recentprojects')

    #get the recent projects
    recent = list(RecentProject.objects.all())
    
    forms = []
    for project in recent[-4:]:
        forms.append((project.id, RecentProjectForm(instance=project)))

    return render_mainpage(request, 'home/recentprojects.html', {"recent": forms[::-1], "new": RecentProjectForm()})
