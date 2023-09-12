from django.urls import path

from bands import views
# from django.urls import path

urlpatterns = [

    path('musician/<int:musician_id>/', views.musician, name="music"),
    path('musicians/', views.musicians, name="musicians"),
    path('band/<int:band_id>/', views.band, name="band"),
    path('bands/', views.bands, name="bands"),

]

# urlpatterns = [
# path('musician/<int:musician_id>/', views.musician, name="musician"),
# ]