from django.contrib.auth.views import LogoutView
from django.urls import *
from login.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('',LoginFormView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(next_page='login'), name="logout"),
]



