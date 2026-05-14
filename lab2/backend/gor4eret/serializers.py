from rest_framework import serializers
from .models import FootballClub


class FootballClubSerializer(serializers.ModelSerializer):
    goal_difference = serializers.IntegerField(read_only=True)

    class Meta:
        model = FootballClub
        fields = (
            "id",
            "name",
            "country",
            "city",
            "founded_on",
            "stadium_name",
            "stadium_capacity",
            "budget_million_eur",
            "website",
            "has_youth_academy",
            "description",
            "wins",
            "losses",
            "draws",
            "goals_scored",
            "goals_conceded",
            "points",
            "goal_difference",
        )
        read_only_fields = ("points", "goal_difference")
