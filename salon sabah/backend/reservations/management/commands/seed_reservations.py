from django.core.management.base import BaseCommand
from faker import Faker
from reservations.models import Reservation, Service
from datetime import datetime, timedelta, time
import random

class Command(BaseCommand):
    help = 'Seed the database with fake reservation data'

    def handle(self, *args, **kwargs):
        fake = Faker('fr_FR')

        services = list(Service.objects.all())
        if not services:
            self.stdout.write(self.style.ERROR("Aucun service trouvé. Veuillez créer des services d'abord."))
            return

        # Générer des réservations pour les 30 prochains jours
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=30)

        # Heures possibles pour les rendez-vous (9h à 17h)
        heures_possibles = [time(h, m) for h in range(9, 18) for m in [0, 30]]

        for _ in range(10):
            service = random.choice(services)
            
            # Générer une date et heure valide
            date_resa = fake.date_between(start_date=start_date, end_date=end_date)
            heure = random.choice(heures_possibles)

            # Formater le numéro de téléphone
            phone_number = f"+33{fake.msisdn()[3:]}"  # Format français

            try:
                Reservation.objects.create(
                    nom=fake.name(),
                    email=fake.email(),
                    telephone=phone_number,
                    service=service,
                    date=date_resa,
                    heure=heure,
                    statut=random.choice([choice[0] for choice in Reservation.STATUT_CHOICES]),
                    commentaire=fake.sentence(nb_words=10)
                )
                self.stdout.write(self.style.SUCCESS(f'Réservation créée pour {service.nom}'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création d'une réservation: {str(e)}"))
                continue

        self.stdout.write(self.style.SUCCESS('✔ Réservations créées avec succès')) 