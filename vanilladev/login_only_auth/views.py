from django.shortcuts import render
from .forms import CustomUserForm

def login(request):
    form = CustomUserForm()
    
    if request.method == 'POST':
        pass

    return render(request, 'login_only_auth/login.html', {'form':form})