from django.core.management.base import BaseCommand
from reservations.models import Service

class Command(BaseCommand):
    help = 'Crée des services de test'

    def handle(self, *args, **kwargs):
        services = [
            {
                'nom': 'Coupe Femme',
                'description': 'Coupe, brushing et mise en forme pour femmes',
                'prix': 45.00,
                'duree': 60
            },
            {
                'nom': 'Coloration',
                'description': 'Coloration professionnelle avec produits de qualité',
                'prix': 65.00,
                'duree': 90
            },
            {
                'nom': 'Coupe Homme',
                'description': 'Coupe et coiffage pour hommes',
                'prix': 25.00,
                'duree': 30
            },
            {
                'nom': 'Brushing',
                'description': 'Brushing et mise en forme',
                'prix': 35.00,
                'duree': 45
            },
            {
                'nom': 'Mèches',
                'description': 'Mèches et balayage personnalisés',
                'prix': 75.00,
                'duree': 120
            }
        ]

        for service_data in services:
            try:
                service, created = Service.objects.get_or_create(
                    nom=service_data['nom'],
                    defaults=service_data
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Service créé : {service.nom}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Service existant : {service.nom}')
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Erreur lors de la création du service {service_data["nom"]}: {str(e)}')
                ) 