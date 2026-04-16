import datetime

from django.db import migrations, models


def recalculate_points(apps, schema_editor):
    FootballClub = apps.get_model("gor4eret", "FootballClub")
    for club in FootballClub.objects.all():
        club.points = club.wins * 3 + club.draws
        club.save(update_fields=["points"])


class Migration(migrations.Migration):

    dependencies = [
        ("gor4eret", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="footballclub",
            options={
                "ordering": ("-points", "-goals_scored", "name"),
                "verbose_name": "football club",
                "verbose_name_plural": "football clubs",
            },
        ),
        migrations.AddField(
            model_name="footballclub",
            name="budget_million_eur",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="footballclub",
            name="city",
            field=models.CharField(default="Unknown city", max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="footballclub",
            name="country",
            field=models.CharField(default="Unknown country", max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="footballclub",
            name="description",
            field=models.TextField(blank=True, default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="footballclub",
            name="founded_on",
            field=models.DateField(default=datetime.date(1900, 1, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="footballclub",
            name="has_youth_academy",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="footballclub",
            name="stadium_capacity",
            field=models.PositiveIntegerField(default=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="footballclub",
            name="stadium_name",
            field=models.CharField(default="Unknown stadium", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="footballclub",
            name="website",
            field=models.URLField(blank=True, default=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="footballclub",
            name="draws",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="footballclub",
            name="goals_conceded",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="footballclub",
            name="goals_scored",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="footballclub",
            name="losses",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="footballclub",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="footballclub",
            name="points",
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name="footballclub",
            name="wins",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RunPython(recalculate_points, migrations.RunPython.noop),
    ]
