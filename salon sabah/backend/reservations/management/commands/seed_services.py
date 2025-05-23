from django.core.management.base import BaseCommand
from faker import Faker
from reservations.models import Service

class Command(BaseCommand):
    help = 'Seed the database with fake service data'

    def handle(self, *args, **kwargs):
        fake = Faker('fr_FR')

        services = [
            {
                'nom': 'Coupe Femme',
                'description': 'Coupe, brushing et mise en forme pour femme',
                'prix': 45.00,
                'duree': 60
            },
            {
                'nom': 'Coupe Homme',
                'description': 'Coupe et coiffage pour homme',
                'prix': 25.00,
                'duree': 30
            },
            {
                'nom': 'Coloration',
                'description': 'Coloration professionnelle avec produits de qualité',
                'prix': 65.00,
                'duree': 90
            },
            {
                'nom': 'Mèches',
                'description': 'Mèches ou balayage pour un effet naturel',
                'prix': 75.00,
                'duree': 120
            },
            {
                'nom': 'Brushing',
                'description': 'Brushing et mise en forme',
                'prix': 30.00,
                'duree': 45
            },
            {
                'nom': 'Soin Profond',
                'description': 'Soin profond revitalisant pour cheveux',
                'prix': 35.00,
                'duree': 45
            }
        ]

        for service_data in services:
            try:
                Service.objects.create(**service_data)
                self.stdout.write(self.style.SUCCESS(f'Service créé : {service_data["nom"]}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Erreur lors de la création du service {service_data["nom"]}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('✔ Services créés avec succès')) 