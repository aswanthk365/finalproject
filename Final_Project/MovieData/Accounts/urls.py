from django.urls import path
from . import views
from . views import *
app_name='Accounts'

urlpatterns = [
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),



]
