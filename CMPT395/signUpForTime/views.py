from django.shortcuts import render
from .forms import SignUpForm


# Create your views here.

def signUp(request):
    form = SignUpForm()
    return render(request, 'signUp/signUp.html', {"form":form})