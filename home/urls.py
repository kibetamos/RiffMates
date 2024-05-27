from django.urls import path
from home import views
from .views import Register, Login

url_patterns = [
    path('login/', views.Login, name="login"),
    path('register/', views.Register, name="register"),
]



    # path('', views.musicians, name="musicians"),

    # path('band/<int:band_id>/', views.band, name="band"),

    # path('bands/', views.bands, name="bands"),
    
    # path('venues/', views.venues, name='venue_list'),

    # path('add_musician/', add_musician_view, name='add_musician')