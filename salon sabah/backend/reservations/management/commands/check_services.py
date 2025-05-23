from django.core.management.base import BaseCommand
from reservations.models import Service

class Command(BaseCommand):
    help = 'Vérifie et crée les services de base'

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

        self.stdout.write("Vérification des services existants...")
        existing_count = Service.objects.count()
        self.stdout.write(f"Nombre de services existants : {existing_count}")

        if existing_count == 0:
            self.stdout.write("Création des services de base...")
            for service_data in services:
                try:
                    Service.objects.create(**service_data)
                    self.stdout.write(self.style.SUCCESS(f"Service créé : {service_data['nom']}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erreur lors de la création du service {service_data['nom']}: {str(e)}"))
        else:
            self.stdout.write("Liste des services existants :")
            for service in Service.objects.all():
                self.stdout.write(f"- {service.nom} ({service.prix}€)") 