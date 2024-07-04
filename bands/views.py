from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect  # Add missing import
from bands.models import Band, Musician, Venue, Room
from .forms import MusicianForm,BandForm
from django.utils.html import format_html 
from django.urls import reverse
from home.views import login




# def index(request):
#     cl = MpesaClient()
#     # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
#     phone_number = '0727824180'
#     amount = 1
#     account_reference = 'reference'
#     transaction_desc = 'Description'
#     callback_url = 'https://darajambili.herokuapp.com/express-payment';
#     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)




def home(request):
    all_bands = Band.objects.all().order_by('name')
    musicians = Musician.objects.all().order_by('last_name')[:6]
    all_musicians = Musician.objects.all()
    number_of_bands = all_bands.count()
    number_of_art = all_musicians.count()
    venues = Venue.objects.all().order_by('name')
    all_venues =  venues.count()
    
    data = {
        'all_venues': all_venues,
        'number_of_art':  number_of_art,
        'number_of_bands': number_of_bands,
        'bands': all_bands,
        'musicians': musicians
    }

    return render(request, "index.html", data)



def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)

    data = {
        "musician": musician,
    }

    return render(request, "musician.html", data)


def musicians(request):
    # Query all musicians ordered by last name
    all_musicians = Musician.objects.all().order_by('id')
    
    # Get the first 6 musicians for the initial display
    musicians = all_musicians[:6]
    
    # Count all musicians
    musicians_count = all_musicians.count()

    # Prepasdsre data to be passed to the template
    data = {
        'all_musicians_count': musicians_count,
        'musicians': musicians,
    }

    return render(request, 'musicians.html', data)


def add_musician_view(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            musician = form.save()
            # Redirect to the musician's detail page
            return redirect('musician_detail', musician_id=musician.id)  # Corrected redirect statement
    else:
        form = MusicianForm()

    return render(request, 'add_musician.html', {'form': form})

def band(request, band_id):
    band = get_object_or_404(Band, id=band_id)

    data = {
        "band": band,
    }

    return render(request, "band.html", data)

# @login
def bands(request):
    # all_bands = Band.objects.all().order_by('name')
    # paginator = Paginator(all_bands, 2)

    # page_num = request.GET.get('page', 1)
    # page_num = int(page_num)

    # if page_num < 1:
    #     page_num = 1
    # elif page_num > paginator.num_pages:
    #     page_num = paginator.num_pages

    # page = paginator.page(page_num)

    # data = {
    #     'bands': page.object_list,
    #     'page': page
    # }
    all_bands = Band.objects.all().order_by('name')
    number_of_bands = all_bands.count()

    
    data = {
        'number_of_bands': number_of_bands,
        'bands': all_bands,
        
    }
    return render(request, 'bands.html', data)



def create_band(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bands')  # Redirect to a list of bands or another page
    else:
        form = BandForm()
    
    return render(request, 'create_band.html', {'form': form})




def venues(request):
    
    venues = Venue.objects.all().order_by('name')
    all_venues =  venues.count()

    data = {
        "venue": venues,
        'all_venues':all_venues
    }

    return render(request, 'venues.html', data)

def rooms(request):
    
    rooms = Room.objects.all()
    all_rooms =  rooms.count()

    data = {
        "room": rooms,

        'all_rooms':all_rooms
    }

    return render(request, 'rooms.html', data)


def initiate_payment(request, room_id):
    cl = MpesaClient()
    phone_number = '0727824180'
    room = Room.objects.get(id=room_id)
    
    # amount = room.price
    amount = int(room.price)
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return JsonResponse(response)

def stk_push_callback(request):
        
        data = request.body
        
        return HttpResponse("STK Push in Django👋")

def musician_detail(request, musician_id):  # Added request parameter
    musician = get_object_or_404(Musician, id=musician_id)

    data = {
        "musician": musician,
    }

    return render(request, "musician_detail.html", data)


# def venues(request):

#     return render(request, 'venues.html')


def pay(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        # Handle the payment logic here
        # For example, process payment and update room status
        return redirect('success')  # Redirect to a success page
    return render(request, 'pay.html', {'room': room})


def success(request):
    return render(request, 'success.html')


