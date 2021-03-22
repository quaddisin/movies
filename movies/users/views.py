from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.admin import User
# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = User(username = username)
        user.set_password(password)
        user.save()
        login(request,user)
        return redirect("index")
    else:

        return render(request,"register.html",{"form":form})

def logins(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password=password)
        if user:
            login(request,user)
            return redirect("index")
    else:

        return render(request,"login.html",{"form":form})

def logouts(request):

    logout(request)
    return redirect("index")