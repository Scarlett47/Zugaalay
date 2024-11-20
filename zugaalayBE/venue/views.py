from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from venue.models import Venue
from venue.serializers import VenueSerializer

class VenueListView(APIView):
    def get(self, request):
        venues = Venue.objects.all()  # Get all venue records
        serializer = VenueSerializer(venues, many=True)  # Serialize the data
        return Response(serializer.data)  # Send the data as a JSON response

    def post(self, request):
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VenueDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            venue = Venue.objects.get(id=id)
            serializer = VenueSerializer(venue)
            return Response(serializer.data)
        except Venue.DoesNotExist:
            return Response({"error": "Venue not found"}, status=404)
