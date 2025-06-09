# Standard library imports
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Third-party imports
from django_daraja.mpesa.core import MpesaClient

# Local imports
from bands.models import Band, Musician, Venue, Room
from .forms import MusicianForm, BandForm


@login_required
def home(request):
    """
    
        Homepage view showing bands, musicians, and venue counts.
    
    """
    context = {
        'bands': Band.objects.all().order_by('name'),
        'featured_musicians': Musician.objects.all().order_by('last_name')[:6],
        'band_count': Band.objects.count(),
        'musician_count': Musician.objects.count(),
        'venue_count': Venue.objects.count(),
    }
    return render(request, "index.html", context)


@login_required
def musician_detail(request, musician_id):
    """
    
        Detail view for a single musician.
    
    """
    musician = get_object_or_404(Musician, id=musician_id)
    return render(request, "musician/musician_detail.html", {'musician': musician})


@login_required
def musicians(request):
    """
    
        List view for all musicians with pagination.
    
    """
    musician_list = Musician.objects.all().order_by('last_name')
    paginator = Paginator(musician_list, 10)  # Show 10 musicians per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'musician/musicians.html', {
        'page_obj': page_obj,
        'total_musicians': musician_list.count()
    })


@login_required
def add_musician(request):
    """
    
        View for adding a new musician.
    
    """
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            musician = form.save()
            messages.success(request, 'Musician added successfully!')
            return redirect('musician_detail', musician_id=musician.id)
    else:
        form = MusicianForm()

    return render(request, 'musician/add_musician.html', {'form': form})


@login_required
def band_detail(request, band_id):
    """
    
        Detail view for a single band.
    
    """
    band = get_object_or_404(Band, id=band_id)
    return render(request, "band/band_detail.html", {'band': band})


@login_required
def bands(request):
    """
    
        List view for all bands.
    
    """
    return render(request, 'band/bands.html', {
        'bands': Band.objects.all().order_by('name'),
        'band_count': Band.objects.count()
    })


@login_required
def create_band(request):
    """
        View for creating a new band.
    
    """
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Band created successfully!')
            return redirect('bands')
    else:
        form = BandForm()
    
    return render(request, 'band/create_band.html', {'form': form})


@login_required
def venues(request):
    """
        List view for all venues.
    
    """
    return render(request, 'venue/venues.html', {
        'venues': Venue.objects.all().order_by('name'),
        'venue_count': Venue.objects.count()
    })


@login_required
def rooms(request):
    """List view for all rooms."""
    return render(request, 'room/rooms.html', {
        'rooms': Room.objects.all(),
        'room_count': Room.objects.count()
    })


@login_required
def initiate_payment(request, room_id):
    """Initiate M-Pesa payment for a room."""
    try:
        room = get_object_or_404(Room, id=room_id)
        cl = MpesaClient()
        
        # In production, get phone number from user profile or form
        response = cl.stk_push(
            phone_number='0727824180',
            amount=int(room.price),
            account_reference='Room Booking',
            transaction_desc=f'Payment for {room.name}',
            callback_url='https://darajambili.herokuapp.com/express-payment'
        )
        
        return JsonResponse({
            'MerchantRequestID': response.MerchantRequestID,
            'CheckoutRequestID': response.CheckoutRequestID,
            'ResponseCode': response.ResponseCode,
            'ResponseDescription': response.ResponseDescription,
            'CustomerMessage': response.CustomerMessage
        })
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
def stk_push_callback(request):
    """Handle M-Pesa callback."""
    # Add proper callback handling logic here
    return HttpResponse("STK Push callback received")


@login_required
def pay(request, room_id):
    """Payment page for a room."""
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'pay.html', {'room': room})


@login_required
def payment_success(request):
    """Payment success page."""
    messages.success(request, 'Payment completed successfully!')
    return render(request, 'payment_success.html')