from django.urls import path
from home import views
from .views import register, login

urlpatterns = [
    path('credits/', views.credits, name="credits"),
    path('news/', views.news, name="news"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]

