from django.contrib import admin
from .models import FootballClub


@admin.register(FootballClub)
class FootballClubAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "country",
        "city",
        "founded_on",
        "wins",
        "losses",
        "draws",
        "points",
        "has_youth_academy",
    )
    search_fields = ("name", "country", "city", "stadium_name")
    list_filter = ("country", "has_youth_academy", "points", "wins")
    readonly_fields = ("points",)
