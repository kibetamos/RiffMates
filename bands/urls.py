from django.urls import path

from bands import views
# from django.urls import path

urlpatterns = [

    path('musician/<int:musician_id>/', views.musician, name="music")
]

# urlpatterns = [
# path('musician/<int:musician_id>/', views.musician, name="musician"),
# ]