from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from datetime import datetime, timedelta
import random
from reservations.models import Service, Reservation, Galerie
from django.core.files import File
from pathlib import Path
import os

class Command(BaseCommand):
    help = 'Génère des données de test pour les réservations et la galerie'

    def handle(self, *args, **kwargs):
        fake = Faker(['fr_FR'])
        
        # Récupérer tous les services
        services = list(Service.objects.all())
        if not services:
            self.stdout.write(self.style.ERROR("Aucun service trouvé. Veuillez d'abord exécuter la commande check_services."))
            return

        # Générer des réservations
        self.stdout.write("Génération des réservations...")
        
        # Date de début : aujourd'hui
        start_date = timezone.now().date()
        
        # Générer des réservations pour les 30 prochains jours
        for _ in range(20):  # 20 réservations
            service = random.choice(services)
            date = start_date + timedelta(days=random.randint(1, 30))
            
            # Heures d'ouverture : 9h à 18h
            hour = random.randint(9, 17)
            minute = random.choice([0, 30])
            
            reservation = Reservation.objects.create(
                nom=fake.name(),
                email=fake.email(),
                telephone=fake.phone_number(),
                service=service,
                date=date,
                heure=f"{hour:02d}:{minute:02d}",
                statut=random.choice(['en_attente', 'confirmee', 'terminee']),
                commentaire=fake.text(max_nb_chars=100) if random.random() > 0.5 else None
            )
            self.stdout.write(self.style.SUCCESS(f"Réservation créée : {reservation}"))

        # Générer des entrées pour la galerie
        self.stdout.write("\nGénération des photos de la galerie...")
        
        titres_galerie = [
            "Coupe moderne femme",
            "Coloration tendance",
            "Coiffure de mariage",
            "Coupe homme stylée",
            "Brushing volume",
            "Mèches naturelles",
            "Coiffure soirée",
            "Soin revitalisant"
        ]
        
        descriptions_galerie = [
            "Une coupe moderne qui met en valeur la personnalité",
            "Des couleurs vibrantes pour un look unique",
            "Coiffure élégante pour votre jour spécial",
            "Style contemporain pour homme",
            "Volume et brillance pour vos cheveux",
            "Des mèches subtiles pour un effet naturel",
            "Coiffure sophistiquée pour vos événements",
            "Soin profond pour des cheveux resplendissants"
        ]

        # Note: Dans un environnement de production, vous devriez avoir de vraies images
        # Pour le moment, nous allons juste créer les entrées dans la base de données
        for titre, description in zip(titres_galerie, descriptions_galerie):
            galerie = Galerie.objects.create(
                titre=titre,
                description=description,
                # Note: l'image devra être ajoutée manuellement
            )
            self.stdout.write(self.style.SUCCESS(f"Photo de galerie créée : {galerie.titre}"))

        self.stdout.write(self.style.SUCCESS(f"\nGénération terminée !\n"))
        self.stdout.write(f"Nombre de réservations créées : {Reservation.objects.count()}")
        self.stdout.write(f"Nombre de photos dans la galerie : {Galerie.objects.count()}") 