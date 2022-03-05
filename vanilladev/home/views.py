from vanilladev.helpers import render_mainpage

# Create your views here.
def index(request):
    return render_mainpage(request, 'home/index.html')
