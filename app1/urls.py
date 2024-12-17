from django.urls import path, include
from .views import *

urlpatterns = [
    path('login', log_in, name = 'login'),
    path('register',register,name ='register'),
    path('logout', log_out, name = 'logout'),
    path('profile',profile,name ='profile'),
    path('home', home, name='home'),
    path('chef', chef, name = 'chef'),
    path('viewer', viewer, name = 'viewer'),
    path('fav',favor , name = 'fav'),
]
