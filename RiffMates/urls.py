
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('home/', include("home.urls")),
    path('admin/', admin.site.urls),
    # path('credits/', home_views.credits, name="credits"),
    # path('news/', home_views.news),
    path('', include("bands.urls"))
]
