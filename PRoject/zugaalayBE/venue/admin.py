from django.contrib import admin
from .models import Venue
from .form import VenueAdminForm

class VenueAdmin(admin.ModelAdmin):
    form = VenueAdminForm
    list_display = ['name', 'location', 'phone']

admin.site.register(Venue, VenueAdmin)
