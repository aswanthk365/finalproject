from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from . models import Movies,Category
from RaitingReview.models import ReviewRating
from django.contrib.auth.decorators import login_required
from . forms import AddMoviesForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.


def index(request,category_slug=None):
    movies = None
    category_page = None

    if category_slug != None:
        category_page = get_object_or_404(Category,slug=category_slug)
        movies = Movies.objects.all().filter(category=category_page)
    else:
        movies = Movies.objects.all()

    #paginator
    pagination=Paginator(movies,10)
    page=request.GET.get('page')
    venues=pagination.get_page(page)

    return render(request,'index.html',{'movies':movies,'category_page':category_page,'movies':venues})


def movie_deatails(request,category_slug,movie_slug):
    movies = Movies.objects.get(category__slug = category_slug,slug = movie_slug)
    reviews = ReviewRating.objects.filter(product_id=movies.id, status=True)
    return render(request,'movie_deatails.html',{'movie_deatails':movies,'r':reviews})


def add_movies(request):
    form = AddMoviesForm()
    if request.method == 'POST':
        form = AddMoviesForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.info(request,"Your Movie Added Sucessfuly.....")
            return redirect('/')
        else:
            messages.info(request,"Deatails are invailded")
            
    context = {
        'form': form
    }
    return render(request,'add_movie.html',context)

def update_movie(request,id):
    movie_id = Movies.objects.get(id=id)
    user=request.user
    form = AddMoviesForm(instance=movie_id)
    if request.method == 'POST':
            form = AddMoviesForm(data=request.POST,files=request.FILES,instance=movie_id)
            if form.is_valid():
                if user == movie_id.user:
                   form.save()
                   return redirect('/')
                else:
                    messages.info(request,"You are not abled to edit the deatils")
            else:  
                 messages.info(request,"This Movie is alredy in the darabase")
    context = {
        'form': form
    }
    return render(request,'update.html',context)

def delete_movie(request,id):
    movie_id = Movies.objects.get(id=id)
    user=request.user
    if user == movie_id.user:
        movie_id.delete()
        messages(request,'movie delelte sucsesfuly......')
    else:
        messages.info(request,"You are not abled to delete this......")
    

