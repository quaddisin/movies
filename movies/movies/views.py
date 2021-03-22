from django.shortcuts import render,redirect
from django.http import request
from movieform.models import AddMovieModel
#from movieform.models import AddMovieModel
def index(request):
    keyword = request.POST.get("search")
    if keyword:
        movies = AddMovieModel.objects.filter(m_name__contains = keyword)
        return render(request,"index.html",{"movies":movies}) 
    else:
        movies = AddMovieModel.objects.all()
        
        return render(request,"index.html",{"movies":movies})
