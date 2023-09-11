from django.urls import path

from bands import views
# from django.urls import path

urlpatterns = [

    path('musician/<int:musician_id>/', views.musician, name="music"),
    path('musicians/', views.musicians, name="musicians"),
]

# urlpatterns = [
# path('musician/<int:musician_id>/', views.musician, name="musician"),
# ]