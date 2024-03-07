from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('add_movie/',views.add_movie,name='add_movie'),
    path('',views.index,name='index'),
    path('add_movies/',views.add_movies,name='add_movie'),
    path('update_movie/<int:id>/',views.update_movie,name='update_movie'),
    # path('delete_movie/<int:id>/',views.delete_movie,name='delete_movie'),
    path('<slug:category_slug>/',views.index,name='category_url'),
    path('<slug:category_slug>/<slug:movie_slug>',views.movie_deatails,name='movie_deatails'),



]
