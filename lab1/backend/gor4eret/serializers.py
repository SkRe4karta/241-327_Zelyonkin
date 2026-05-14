from rest_framework import serializers
from .models import FootballClub


class FootballClubSerializer(serializers.ModelSerializer):
    goal_difference = serializers.IntegerField(read_only=True)

    class Meta:
        model = FootballClub
        fields = "__all__"
        read_only_fields = ("points", "goal_difference")
