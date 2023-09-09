from django.shortcuts import render

# Create your views here.
# RiffMates/bands/views.py
from django.shortcuts import render, get_object_or_404 #1

from bands.models import Musician #2

def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id) #3
    
    data = {
        "musician": musician, #4
            }
    
    return render(request, "musician.html", data)