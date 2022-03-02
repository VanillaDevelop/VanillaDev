from .forms import ProjectForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

#add project - requires login
@login_required()
def add(request):
    #POST - save project
    if request.method == "POST":
        form = ProjectForm(request.POST)
        #if form is valid, redirect to the corresponding post
        if form.is_valid():
            post = form.save()
            return redirect('blog:post', post.id)
        else:
            #serve the sent form again
            return render(request, 'projects/change.html', {"form":form})

    #GET - display empty blog post
    form = ProjectForm()
    return render(request, 'projects/change.html', {"form":form})