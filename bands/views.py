from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404 #1

from bands.models import Musician

def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id) 

    data = {
        "musician": musician,
            }
    
    return render(request, "musician.html", data)