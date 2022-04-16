import math
from vanilladev.helpers import render_mainpage
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from .models import Image

#upload file - requires login
@login_required()
def add(request):
    #POST - save image
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        #if form is valid, redirect to the overview
        #TODO not implemented yet
        if form.is_valid():
            image = form.save()
            return redirect('media:overview')
        else:
            #serve the sent form again
            return render_mainpage(request, 'media/change.html', {"form":form})

    #GET - display empty image upload page
    form = ImageForm()
    return render_mainpage(request, 'media/change.html', {"form":form})

#view images - requires login
@login_required()
def overview(request, pageno=1):
    images = Image.objects.all().order_by('-created_at', '-id')
    #we display 12 images per page
    pagecount = math.ceil(images.count()/12)
    #fixes an infinite loop if there are 0 images
    if pagecount < 1: pagecount = 1
    #if the requested page number is > pagecount or < 1, opt for the last/first page
    if pageno > pagecount: return redirect('media:overview', pagecount)
    if pageno < 1: return redirect('media:overview', 1)
    #select the images corresponding to the page number and return them. 
    return render_mainpage(request, 'media/overview.html', {"images": images[6*(pageno-1):6*(pageno)], "pagecount":pagecount, "pageno":pageno, "pages":range(1, pagecount+1)})

#delete image - requires login
@login_required()
def delete(request, id):
    #if post request (which passed CSRF)
    if request.method == "POST":
        #try to delete post with given ID
        try:
            img = Image.objects.get(id=id)
            img.file.delete()
            img.delete()
        except:
            #exceptions don't really matter here
            pass

    #redirect the user to the media overview
    return redirect('media:overview')

#edit image - requires login
@login_required()
def edit(request, id):
    #POST - save image
    if request.method == "POST":
        image = get_object_or_404(Image, id=id)
        form = ImageForm(request.POST, request.FILES, instance=image)
        #if form is valid, redirect to the corresponding post
        if form.is_valid():
            form.save()
            return redirect('media:overview')
        else: 
            #serve the sent form again
            return render_mainpage(request, 'media/change.html', {"form":form})

    #GET - show edit form for blog post
    image = get_object_or_404(Image, id=id)
    form = ImageForm(instance=image)
    return render_mainpage(request, 'media/change.html', {"form":form})