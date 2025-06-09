from django.urls import path
from django.contrib.auth.views import LogoutView
from home import views

app_name = 'home'  # Add namespace for your app

urlpatterns = [



        # Authentication URLs
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.user_logout, name='logout'),


    
    # Public pages
    path('credits/', views.credits, name="credits"),
    path('news/', views.news, name="news"),
    

    
    # Alternative logout implementation (Django built-in)
    # path('logout/', LogoutView.as_view(next_page='home:login'), name='logout'),
]