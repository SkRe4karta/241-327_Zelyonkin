from django.core.exceptions import ValidationError
from django.db import models


class FootballClub(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    founded_on = models.DateField()
    stadium_name = models.CharField(max_length=200)
    stadium_capacity = models.PositiveIntegerField()
    budget_million_eur = models.DecimalField(max_digits=8, decimal_places=2)
    website = models.URLField(blank=True)
    has_youth_academy = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        ordering = ("-points", "-goals_scored", "name")
        verbose_name = "football club"
        verbose_name_plural = "football clubs"

    def __str__(self):
        return f"{self.name} ({self.country})"

    @property
    def goal_difference(self):
        return self.goals_scored - self.goals_conceded

    def clean(self):
        if self.founded_on.year < 1850:
            raise ValidationError({"founded_on": "Foundation date looks unrealistic for a football club."})
        if self.goals_conceded > 200 or self.goals_scored > 200:
            raise ValidationError("Goals look unrealistic for a single season.")

    def save(self, *args, **kwargs):
        self.points = self.wins * 3 + self.draws
        super().save(*args, **kwargs)
