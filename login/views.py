from django.shortcuts import render,redirect
from Blog.models import Blog
from login.models import User

def index2(request):
    pass
    return render(request,'index2.html')

def login(request):
    pass
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect('/index/')

