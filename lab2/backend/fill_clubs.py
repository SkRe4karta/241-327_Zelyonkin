#!/usr/bin/env python
import argparse
import os
import random
import sys
from decimal import Decimal
from pathlib import Path

import django
from django.db import transaction
from faker import Faker


def setup_django():
    project_root = Path(__file__).resolve().parent
    sys.path.insert(0, str(project_root))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab2.settings")
    django.setup()


def generate_football_clubs(count: int, reset: bool):
    from gor4eret.models import FootballClub

    fake = Faker()

    countries = [
        "England",
        "Spain",
        "Germany",
        "Italy",
        "France",
        "Portugal",
        "Netherlands",
        "Brazil",
        "Argentina",
        "Russia",
    ]

    club_words = [
        "United",
        "City",
        "Rovers",
        "Athletic",
        "Sporting",
        "Dynamo",
        "Real",
        "Inter",
        "Olympic",
        "Victory",
    ]

    with transaction.atomic():
        if reset:
            deleted_count, _ = FootballClub.objects.all().delete()
            print(f"Deleted clubs: {deleted_count}")

        for i in range(count):
            city = fake.city()
            name = f"{city} {random.choice(club_words)} {i + 1}"

            wins = random.randint(0, 30)
            draws = random.randint(0, 15)
            losses = random.randint(0, 30)

            club = FootballClub(
                name=name,
                country=random.choice(countries),
                city=city,
                founded_on=fake.date_between(start_date="-150y", end_date="-5y"),
                stadium_name=f"{fake.city()} Arena",
                stadium_capacity=random.randint(5000, 100000),
                budget_million_eur=Decimal(str(round(random.uniform(1, 900), 2))),
                website=f"https://{fake.domain_name()}",
                has_youth_academy=random.choice([True, False]),
                description=fake.text(max_nb_chars=300),
                wins=wins,
                losses=losses,
                draws=draws,
                goals_scored=random.randint(0, 120),
                goals_conceded=random.randint(0, 120),
            )

            club.save()

    print(f"Created clubs: {count}")
    print(f"Total clubs in database: {FootballClub.objects.count()}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate demo football clubs for lab work #2."
    )
    parser.add_argument(
        "--count",
        type=int,
        default=150,
        help="How many clubs to generate.",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Delete existing clubs before seeding.",
    )

    args = parser.parse_args()

    setup_django()
    generate_football_clubs(count=args.count, reset=args.reset)


if __name__ == "__main__":
    main()