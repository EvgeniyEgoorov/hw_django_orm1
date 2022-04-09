import csv

from django.core.management.base import BaseCommand
from work_with_database.phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_info = Phone(
                name=phone['name'],
                price=int(phone['price']),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exist=phone['lte_exist'],
                slug=phone['name'].lower()
            )
            phone_info.save()
