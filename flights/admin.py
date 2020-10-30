from  django.contrib import admin
from . models import Flight ,Airport ,Passenger
# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display= ("origin","id","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=('flights',)

admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger,PassengerAdmin)
admin.site.register(Airport)
