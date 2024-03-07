from django.shortcuts import render
from django.db.models import Q
from MovieApp.models import Movies
from django.urls import reverse

# Create your views here.


def search(request):
    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        if query:
            movies=Movies.objects.all().filter(Q(movie_tittle__contains=query) | Q(category__movie_category__contains=query))
        return render(request,'search.html',{'query':query,'movies':movies})
    
