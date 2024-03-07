from django.urls import path
from . import views
from . views import *

app_name = 'Review'


urlpatterns = [
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),

]




