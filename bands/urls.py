from django.urls import path
from bands import views
# from django.urls import path
from .views import add_musician_view, musician_detail, home, create_band, rooms, stk_push_callback


urlpatterns = [
    
    # path('', views.index, name='index'),

   path('pay/<int:room_id>/', views.initiate_payment, name='initiate_payment'),

    path('stk-push-callback/', views.stk_push_callback, name='stk_push_callback'),

    path('', home, name='home'),
    
    path('musicians/', views.musicians, name="musicians"),

    path(' 1', add_musician_view, name='add_musician'),

    path('musician_detail/<int:id>/', musician_detail, name='musician_detail'),

    path('musician/<int:musician_id>/', views.musician, name="musician"),


    path('band/<int:band_id>/', views.band, name="band"),

    path('bands/', views.bands, name="bands"),
    
    path('create_band/', create_band, name='create_band'),


    path('venues/', views.venues, name='venues'),

    path('rooms/', views.rooms, name='rooms'),

    path('pay/<int:room_id>/', views.pay, name='pay'),
    path('success/', views.success, name='success')

]
