from django.contrib import admin
from . models import Category,Movies
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('movie_category',)}
admin.site.register(Category,CategoryAdmin)

class MoviesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('movie_tittle',)}
admin.site.register(Movies,MoviesAdmin)

# admin.site.register(ReviewRating)