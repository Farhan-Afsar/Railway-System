from django.contrib import admin
from .models import Train, Passenger, Schedule, Ticket, Station, Route

admin.site.register(Train)
admin.site.register(Passenger)
admin.site.register(Schedule)
admin.site.register(Ticket)
admin.site.register(Station)
admin.site.register(Route)
