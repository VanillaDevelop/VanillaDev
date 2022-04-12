from vanilladev.helpers import render_mainpage
from django.contrib.auth.decorators import login_required
from .forms import RecentProjectForm
from .models import RecentProject

# Create your views here.
def index(request):
    return render_mainpage(request, 'home/index.html')

#change recent projects
@login_required()
def recentprojects(request):
    #get the recent projects
    recent = list(RecentProject.objects.all())

    #if there are less than 4 recent projects
    if(len(recent) < 4):
        #create 4 filler projects
        for _ in range(4 - len(recent)):
            newproj = RecentProject(title="", icon="", type="", description="", link="")
            newproj.save()
            recent.append(newproj)
    
    forms = []
    for project in recent:
        forms.append(RecentProjectForm(instance=project))

    return render_mainpage(request, 'home/recentprojects.html', {"recent": forms})
