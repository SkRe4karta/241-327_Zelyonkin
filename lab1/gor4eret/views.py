from rest_framework import filters, viewsets
from .models import FootballClub
from .serializers import FootballClubSerializer


class FootballClubViewSet(viewsets.ModelViewSet):
    queryset = FootballClub.objects.all()
    serializer_class = FootballClubSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name", "country", "city", "stadium_name")
    ordering_fields = ("name", "country", "city", "points", "wins", "founded_on")
