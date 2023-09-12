from django.contrib import admin

# Register your models here.
from bands.models import Musician


@admin.register(Musician)

class MusicianAdmin(admin.ModelAdmin):
    pass