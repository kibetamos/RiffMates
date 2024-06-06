from django.urls import path
from bands import views
# from django.urls import path
from .views import add_musician_view, musician_detail, home, create_band


urlpatterns = [

    path('', home, name='home'),

    path('musicians/', views.musicians, name="musicians"),

    path(' 1', add_musician_view, name='add_musician'),

    path('musician_detail/<int:id>/', musician_detail, name='musician_detail'),

    path('musician/<int:musician_id>/', views.musician, name="musician"),


    path('band/<int:band_id>/', views.band, name="band"),

    path('bands/', views.bands, name="bands"),
    
    path('create_band/', create_band, name='create_band'),


    path('venues/', views.venues, name='venue_list')

]
