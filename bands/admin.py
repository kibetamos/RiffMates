from django.contrib import admin
from datetime import datetime, date  
# Register your models here.
from datetime import datetime, date


from bands.models import Musician, Venue, Room

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'show_weekday')
    search_fields = ("last_name", "first_name", )

    def show_weekday(self, obj):
        # Fetch weekday of artist's birth
        return obj.birth.strftime("%A")
    
    show_weekday.short_description = "Birth Weekday"

class DecadeListFilter(admin.SimpleListFilter):
    title = 'decade born'
    parameter_name = 'decade'

    def lookups(self, request, model_admin):

        result = []
        this_year = datetime.today().year

        this_decade = (this_year // 10) * 10 

        start = this_decade - 10
        for year in range(start, start - 100, -10): 

            result.append( (str(year), f"{year}-{year+9}") ) 
        return result



@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
