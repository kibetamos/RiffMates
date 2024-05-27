from django.urls import path
from home import views
from .views import Register, Login

urlpatterns = [
    path('credits/', views.credits, name="credits"),
    path('news/', views.news, name="news"),
    path('login/', views.Login, name="login"),
    path('register/', views.Register, name="register"),
]

