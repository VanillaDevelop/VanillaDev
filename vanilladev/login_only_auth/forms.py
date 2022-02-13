from django.forms import ModelForm
from .models import User

class CustomUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']