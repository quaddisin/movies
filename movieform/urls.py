from django.contrib import admin
from django.urls import path,include
from .views import addmovie,action,scifi,horror,drama,moviedetails
app_name = "movie"

urlpatterns = [
    path("addmovie/",addmovie,name="addmovie"),
    path("action/",action,name="action"),
    path("scifi/",scifi,name="scifi"),
    path("horror/",horror,name="horror"),
    path("drama/",drama,name="drama"),
    path("moviedetails/<str:m_name>",moviedetails,name="moviedetails")
]
