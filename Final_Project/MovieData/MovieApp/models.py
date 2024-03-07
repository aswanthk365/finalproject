from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
# Create your models here.


class Category(models.Model):
    movie_category = models.CharField(unique=True,max_length=200)
    slug = models.SlugField(unique=True,max_length=200)

    def get_url(self):
        return reverse('category_url',args=[self.slug]) 

    def __str__(self):
        return self.slug
    
class Movies(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,models.CASCADE)
    movie_tittle = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='movie_tittle',unique=True,max_length=200,null=True,default=None,editable=True)
    movie_poster = models.ImageField(upload_to='movie_posters',default='staric/images/a.jpg')
    movie_trailer = models.CharField(max_length=200)
    description = models.TextField()
    relese_date = models.DateField()
    actors = models.CharField(max_length=300)

    def get_url(self):
        return reverse('movie_deatails',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.movie_tittle
    

# class ReviewRating(models.Model):
#     movie = models.ForeignKey(Movies,on_delete = models.CASCADE)
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     subject = models.CharField(max_length=100, blank = True)
#     review = models.TextField(max_length=500, blank = True)
#     rating = models.FloatField()
#     ip = models.CharField(max_length=100, blank = True)
#     status  = models.BooleanField(default = True)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now_add = True)

#     def __str__(self):
#         return self.user.username

