from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render, get_object_or_404 #1

from bands.models import Musician

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




    # data = {
    #     'musicians':Musician.objects.all().order_by('last_name'),
    #     }
    # return render(request, "musicians.html", data)