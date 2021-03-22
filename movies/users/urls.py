from django.urls import path
from .views import register,logins,logouts
app_name = "users"

urlpatterns = [
    path("register/",register,name="register"),
    path("login/",logins,name="login"),
    path("logout/",logouts,name="logout")
]
