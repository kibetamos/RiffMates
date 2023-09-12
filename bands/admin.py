from django.contrib import admin

# Register your models here.

from bands.models import Musician, Venue, Room

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'show_weekday')
    search_fields = ("last_name", "first_name", )

    def show_weekday(self, obj):
        # Fetch weekday of artist's birth
        return obj.birth.strftime("%A")
    
    show_weekday.short_description = "Birth Weekday"

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
