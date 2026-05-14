import random
from decimal import Decimal

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.text import slugify
from faker import Faker

from gor4eret.models import FootballClub

COUNTRIES = [
    "England",
    "Germany",
    "Spain",
    "Italy",
    "France",
    "Portugal",
    "Netherlands",
    "Turkey",
    "Russia",
    "Belgium",
]

SUFFIXES = [
    "United",
    "City",
    "Athletic",
    "Sporting",
    "Dynamo",
    "Olympic",
    "Rovers",
    "FC",
]


class Command(BaseCommand):
    help = "Generate 100+ football clubs with random realistic data for lab work."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=150, help="Number of clubs to create.")
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete existing football clubs before generating a new dataset.",
        )

    def handle(self, *args, **options):
        count = options["count"]
        if count < 100:
            raise CommandError("Для ЛР1 нужно сгенерировать не менее 100 записей.")

        fake = Faker("en_US")
        random.seed(42)
        Faker.seed(42)

        if options["reset"]:
            deleted_count, _ = FootballClub.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Удалено записей перед генерацией: {deleted_count}"))

        existing_names = set(FootballClub.objects.values_list("name", flat=True))
        clubs_to_create = []

        with transaction.atomic():
            while len(clubs_to_create) < count:
                city = fake.city()
                suffix = random.choice(SUFFIXES)
                name = f"{city} {suffix}"
                if name in existing_names:
                    continue

                existing_names.add(name)
                matches = random.randint(26, 38)
                wins = random.randint(0, matches)
                draws = random.randint(0, matches - wins)
                losses = matches - wins - draws
                goals_scored = random.randint(22, 98)
                goals_conceded = random.randint(18, 78)
                budget = Decimal(random.randint(20, 450)) + Decimal(random.randint(0, 99)) / Decimal("100")
                website_slug = slugify(name)

                clubs_to_create.append(
                    FootballClub(
                        name=name,
                        country=random.choice(COUNTRIES),
                        city=city,
                        founded_on=fake.date_between(start_date="-120y", end_date="-5y"),
                        stadium_name=f"{fake.last_name()} Arena",
                        stadium_capacity=random.randint(12000, 90000),
                        budget_million_eur=budget,
                        website=f"https://{website_slug}.example.com",
                        has_youth_academy=random.random() > 0.25,
                        description=fake.sentence(nb_words=12),
                        wins=wins,
                        losses=losses,
                        draws=draws,
                        goals_scored=goals_scored,
                        goals_conceded=goals_conceded,
                        points=wins * 3 + draws,
                    )
                )

            FootballClub.objects.bulk_create(clubs_to_create, batch_size=200)

        total = FootballClub.objects.count()
        self.stdout.write(self.style.SUCCESS(f"Успешно создано {len(clubs_to_create)} клубов."))
        self.stdout.write(self.style.SUCCESS(f"Всего клубов в базе: {total}."))
