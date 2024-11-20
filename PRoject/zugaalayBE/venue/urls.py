from django.urls import path
from .views import VenueListView
from .views import VenueDetailView

urlpatterns = [
    path('venues/', VenueListView.as_view(), name='venue-list'),
    path('venues/<int:id>/', VenueDetailView.as_view(), name='venue-detail'),

]
