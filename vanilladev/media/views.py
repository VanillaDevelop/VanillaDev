import math
from vanilladev.helpers import render_mainpage
from django.shortcuts import redirect
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
