from vanilladev.helpers import render_mainpage
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageForm


#upload file - requires login
@login_required()
def add(request):
    #POST - save image
    if request.method == "POST":
        form = ImageForm(request.POST)
        #if form is valid, redirect to the overview
        #TODO not implemented yet
        if form.is_valid():
            image = form.save()
            return redirect('base:index')
        else:
            #serve the sent form again
            return render_mainpage(request, 'media/change.html', {"form":form})

    #GET - display empty image upload page
    form = ImageForm()
    return render_mainpage(request, 'media/change.html', {"form":form})