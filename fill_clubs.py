#!/usr/bin/env python
import argparse
import os
import sys
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parent / "lab1"
    sys.path.insert(0, str(project_root))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab1.settings")

    import django
    from django.core.management import call_command

    parser = argparse.ArgumentParser(description="Generate demo football clubs for lab work #1.")
    parser.add_argument("--count", type=int, default=150, help="How many clubs to generate.")
    parser.add_argument("--reset", action="store_true", help="Delete existing clubs before seeding.")
    args = parser.parse_args()

    django.setup()
    call_command("seed_football_clubs", count=args.count, reset=args.reset)


if __name__ == "__main__":
    main()
