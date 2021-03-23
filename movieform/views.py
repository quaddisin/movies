from django.shortcuts import render,redirect
from .models import AddMovieModel
# Create your views here
from .forms import MovieForm
def addmovie(request):
    
    form = MovieForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    else:

        return render(request,"addmovie.html",{"form":form})

def action(request):
    movies = AddMovieModel.objects.filter(m_kind="Action")
    if movies:
        return render(request,"moviekind/action.html",{"movies":movies})
    else:
        return render(request,"moviekind/action.html")


def scifi(request):
    movies = AddMovieModel.objects.filter(m_kind="Sci-Fi")
    if movies:
        return render(request,"moviekind/scifi.html",{"movies":movies})
    else:
        return render(request,"moviekind/scifi.html")

def horror(request):
    movies = AddMovieModel.objects.filter(m_kind="Horror")
    if movies:
        return render(request,"moviekind/horror.html",{"movies":movies})
    else:
        return render(request,"moviekind/horror.html")

def drama(request):
    movies = AddMovieModel.objects.filter(m_kind="Drama")
    if movies:
        return render(request,"moviekind/drama.html",{"movies":movies})
    else:
        return render(request,"moviekind/drama.html")

def moviedetails(request,m_name):
    movies = AddMovieModel.objects.filter(m_name=m_name).first
    return render(request,"moviedetails.html",{"movies":movies})