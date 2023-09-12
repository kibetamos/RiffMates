from django.urls import path

from bands import views
# from django.urls import path

urlpatterns = [

    path('musician/<int:musician_id>/', views.musician, name="musician"),

    path('musicians/', views.musicians, name="musicians"),

    path('band/<int:band_id>/', views.band, name="band"),
    path('bands/', views.bands, name="bands"),
    path('venues/', views.venues, name='venue_list'),

]

# urlpatterns = [
# path('musician/<int:musician_id>/', views.musician, name="musician"),
# ]