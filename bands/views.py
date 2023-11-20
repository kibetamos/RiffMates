from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render, get_object_or_404 #1

from bands.models import Band, Musician, Venue
from .forms import MusicianForm 





def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id) 

    data = {
        "musician": musician,
            }
    
    return render(request, "musician.html", data)


def musicians(request):
    all_musicians = Musician.objects.all().order_by('last_name')
    paginator = Paginator(all_musicians, 2)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)

    if page_num < 1:
        page_num =1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num)

    data =  {
        'musicians':page.object_list,
        'page':page
    }

    return render(request,'musicians.html',data)




def band(request, band_id):
    band = get_object_or_404(Band, id=band_id) 

    data = {
        "band": band,
            }
    
    return render(request, "band.html", data)


def bands(request):
    all_bands = Band.objects.all().order_by('name')
    paginator = Paginator(all_bands, 2)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)

    if page_num < 1:
        page_num =1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num)

    data =  {
        'bands':page.object_list,
        'page':page
    }

    return render(request,'bands.html',data)

    # data = {
    #     'musicians':Musician.objects.all().order_by('last_name'),
    #     }
    # return render(request, "musicians.html", data)


def venues(request):
    venues = Venue.objects.all().order_by('name')

    return render(request, 'venue_list.html', {'venues': venues})




def add_musician_view(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            # Save the musician to the database
            musician = form.save()
            # Redirect to the musician's detail page or any other desired page
            return render('musician_detail', id=musician.id)
    else:
        form = MusicianForm()

    return render(request, 'add_musician.html', {'form': form})