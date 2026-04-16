from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import FootballClub


class FootballClubApiTests(APITestCase):
    def setUp(self):
        self.club = FootballClub.objects.create(
            name="FC Test City",
            country="Russia",
            city="Moscow",
            founded_on=date(1998, 5, 12),
            stadium_name="North Arena",
            stadium_capacity=42000,
            budget_million_eur="85.50",
            website="https://test-city.example.com",
            has_youth_academy=True,
            description="Reference club for API tests.",
            wins=18,
            losses=4,
            draws=8,
            goals_scored=57,
            goals_conceded=31,
        )

    def test_list_returns_seeded_object(self):
        response = self.client.get(reverse("footballclub-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], self.club.name)
        self.assertEqual(response.data[0]["points"], 62)

    def test_create_calculates_points_automatically(self):
        payload = {
            "name": "FC API United",
            "country": "Germany",
            "city": "Berlin",
            "founded_on": "2004-08-17",
            "stadium_name": "API Arena",
            "stadium_capacity": 38000,
            "budget_million_eur": "61.25",
            "website": "https://api-united.example.com",
            "has_youth_academy": False,
            "description": "Created from API tests.",
            "wins": 20,
            "losses": 6,
            "draws": 4,
            "goals_scored": 64,
            "goals_conceded": 29,
        }

        response = self.client.post(reverse("footballclub-list"), payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["points"], 64)
        self.assertEqual(response.data["goal_difference"], 35)

    def test_retrieve_returns_single_club(self):
        response = self.client.get(reverse("footballclub-detail", args=[self.club.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["country"], "Russia")

    def test_patch_updates_points(self):
        response = self.client.patch(
            reverse("footballclub-detail", args=[self.club.pk]),
            {"wins": 19, "draws": 7},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["points"], 64)

    def test_delete_removes_club(self):
        response = self.client.delete(reverse("footballclub-detail", args=[self.club.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(FootballClub.objects.filter(pk=self.club.pk).exists())
