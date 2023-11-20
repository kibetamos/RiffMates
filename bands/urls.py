from django.urls import path
from .views import add_musician_view
from bands import views
# from django.urls import path

urlpatterns = [

    path('musician/<int:musician_id>/', views.musician, name="musician"),

    path('', views.musicians, name="musicians"),

    path('band/<int:band_id>/', views.band, name="band"),

    path('bands/', views.bands, name="bands"),
    
    path('venues/', views.venues, name='venue_list'),

    path('add_musician/', add_musician_view, name='add_musician'),

]

# urlpatterns = [
# path('musician/<int:musician_id>/', views.musician, name="musician"),
# ]