from django.contrib import admin

# Register your models here.

from bands.models import Musician, Venue, Room

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'show_weekday')
    # pass

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
