
from django.contrib import admin
from django.urls import path, include 
from bands.views import home 

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('bands/', include('bands.urls')),
    path('accounts/', include('home.urls')),  # For auth
]

