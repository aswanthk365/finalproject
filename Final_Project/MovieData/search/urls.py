from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('search_result/',views.search,name='search_result'),
]
