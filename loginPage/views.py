from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def landingpage(request):
    return render(request, 'loginPage/index.html')

def signup(request):
    return render(request, 'loginPage/signup.html')

def signin(request):
    return render(request, 'loginPage/signin.html')

def signout(request):
    # return render(request, 'signout.html')
    pass