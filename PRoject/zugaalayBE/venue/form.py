from django import forms
from .models import Venue
import base64

class VenueAdminForm(forms.ModelForm):
    image_upload = forms.ImageField(required=False, label="Upload Image")

    class Meta:
        model = Venue
        fields = ['name', 'description', 'location', 'phone', 'image_upload','lat' ,'long' ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        uploaded_image = self.cleaned_data.get('image_upload')

        if uploaded_image:
            # Convert uploaded image to Base64
            instance.base64image = base64.b64encode(uploaded_image.read()).decode('utf-8')

        if commit:
            instance.save()
        return instance
