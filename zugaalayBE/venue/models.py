from django.db import models
import base64

class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)  # Name of the venue
    description = models.TextField(blank=True)  # Optional description
    location = models.CharField(max_length=255)  # Location of the venue
    base64image = models.TextField(blank=True, null=True)  # Base64-encoded image
    phone = models.CharField(max_length=15, blank=True)  # Optional phone number
    lat = models.DecimalField(max_digits=25, decimal_places=20, default=0.0)
    long = models.DecimalField(max_digits=25, decimal_places=20, default=0.0)  # Longitude field
    def __str__(self):
        return self.name
