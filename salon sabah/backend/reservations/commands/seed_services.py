from django.core.management.base import BaseCommand
from faker import Faker
from salon.models import Service  # adapte selon le nom de ton app

class Command(BaseCommand):
    help = 'Seed the database with fake services'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # crée 10 services
            service = Service.objects.create(
                nom=fake.word().capitalize(),
                description=fake.text(max_nb_chars=200),
                prix=round(fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=10, max_value=100), 2),
                duree=fake.random_int(min=15, max=120)
            )
            self.stdout.write(self.style.SUCCESS(f'Service créé : {service.nom}'))
