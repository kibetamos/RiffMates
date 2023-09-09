from django.urls import path

from bands import views

urlpattern = [

    path('musician/<int:musician_id>/', views.musician, name="music")
]