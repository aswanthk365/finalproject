from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MovieApp.urls')),
    path('accounts/',include('Accounts.urls')),
    path('review/',include('RaitingReview.urls')), 
    path('search/',include('search.urls')),   
  
  
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

