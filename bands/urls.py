from django.urls import path
from bands import views

app_name = 'bands'  # Add namespace for your app

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Musician URLs
    path('musicians/', views.musicians, name='musicians'),
    path('musicians/add/', views.add_musician, name='add_musician'),
    path('musicians/<int:musician_id>/', views.musician_detail, name='musician_detail'),
    
    # Band URLs
    path('bands/', views.bands, name='bands'),
    path('bands/create/', views.create_band, name='create_band'),
    path('bands/<int:band_id>/', views.band_detail, name='band_detail'),
    
    # Venue/Room URLs
    path('venues/', views.venues, name='venues'),
    path('rooms/', views.rooms, name='rooms'),
    
    # Payment URLs
    path('rooms/pay/<int:room_id>/', views.pay, name='pay'),
    path('rooms/initiate-payment/<int:room_id>/', views.initiate_payment, name='initiate_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('stk-push-callback/', views.stk_push_callback, name='stk_push_callback'),
]