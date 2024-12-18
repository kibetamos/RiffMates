# Register your models here.
from django.contrib import admin
from datetime import datetime, date  
from datetime import datetime, date
from django.utils.html import format_html 
from django.urls import reverse
from bands.models import Band, Musician, Venue, Room

# class DecadeListFilter(admin.SimpleListFilter):
#     title = 'decade born'
#     parameter_name = 'decade'

#     def lookups(self, request, model_admin):
#         result = []
#         this_year = datetime.today().year

#         this_decade = (this_year // 10) * 10 

#         start = this_decade - 10
#         for year in range(start, start - 100, -10): 

#             result.append( (str(year), f"{year}-{year+9}") ) 
#         return result
    

#     def queryset(self, request, queryset):
#         start = self.value() 
#         if start is None:
#             return queryset
#         start = int(start)
#         result = queryset.filter(
#             birth__gte=date(start, 1, 1), #9
#             birth__lte=date(start + 9, 12, 31),
#             )
#         return result

# @admin.register(Musician)
# class MusicianAdmin(admin.ModelAdmin):
#     list_display = ('id', 'last_name', 'first_name', 'birth', 'show_weekday','show_bands')
#     list_filter = (DecadeListFilter, )
#     search_fields = ("last_name", "first_name", )

#     def show_bands(self, obj):
#         bands = obj.band_set.all()
#         if len(bands) == 0: 

#             return format_html("<i>None</i>")
        
#         plural = "" 
#         if len(bands) > 1:
#             plural = "s"
#         parm = "?id__in=" + ",".join([str(b.id) for b in bands]) 
#         url = reverse("admin:bands_band_changelist") + parm 
#         return format_html('<a href="{}">Band{}</a>', url, plural)
#     show_bands.short_description = "Bands"

#     def show_weekday(self, obj):
#         # Fetch weekday of artist's birth
#         return obj.birth.strftime("%A")
    
#     show_weekday.short_description = "Birth Weekday"

# @admin.register(Band)
# class BandAdmin(admin.ModelAdmin):

#     list_display = ('id', 'name')
#     # list_filter = (DecadeListFilter, )
#     # search_fields = ("name", "musicians")
    
    
# @admin.register(Venue)
# class VenueAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     pass
from django.contrib import admin
from .models import Band, Musician, Venue, Room, Performance

admin.site.register(Band)
admin.site.register(Musician)
admin.site.register(Venue)
admin.site.register(Room)
admin.site.register(Performance)
