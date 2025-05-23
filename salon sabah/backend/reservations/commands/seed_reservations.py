from django.core.management.base import BaseCommand
from faker import Faker
from reservations.models import Reservation, Service
from datetime import datetime, timedelta
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

        for _ in range(10):
            service = random.choice(services)
            
            # Générer une date et heure valide
            date_resa = fake.date_between(start_date=start_date, end_date=end_date)
            heure = fake.time_object(end_datetime=None, start=9, end=17)  # Entre 9h et 17h

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
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Erreur lors de la création d'une réservation: {str(e)}"))
                continue

        self.stdout.write(self.style.SUCCESS('✔ Réservations créées avec succès'))
