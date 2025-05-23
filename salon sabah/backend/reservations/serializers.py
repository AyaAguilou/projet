from rest_framework import serializers
from .models import Service, Reservation, Galerie
from datetime import datetime, time, timedelta

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'nom', 'description', 'prix', 'duree', 'image']

class ReservationSerializer(serializers.ModelSerializer):
    service_nom = serializers.CharField(source='service.nom', read_only=True)
    
    class Meta:
        model = Reservation
        fields = ['id', 'nom', 'email', 'telephone', 'service', 'service_nom',
                 'date', 'heure', 'statut', 'commentaire', 'date_creation',
                 'date_modification']
        read_only_fields = ['date_creation', 'date_modification']

    def validate(self, data):
        """
        Vérification des contraintes de réservation
        """
        # Vérifier que la date n'est pas dans le passé
        if data.get('date'):
            if data['date'] < datetime.now().date():
                raise serializers.ValidationError({"date": "La date ne peut pas être dans le passé."})

        # Vérifier les horaires d'ouverture (9h-18h)
        if data.get('heure'):
            heure = data['heure']
            ouverture = time(9, 0)  # 9h00
            fermeture = time(18, 0)  # 18h00
            
            if heure < ouverture or heure > fermeture:
                raise serializers.ValidationError(
                    {"heure": "Les réservations sont possibles uniquement entre 9h et 18h."}
                )

        # Vérifier la disponibilité du créneau
        if data.get('date') and data.get('heure') and data.get('service'):
            service = data['service']
            date_resa = data['date']
            heure_resa = data['heure']
            duree = timedelta(minutes=service.duree)
            
            # Calculer l'heure de fin
            heure_debut = datetime.combine(date_resa, heure_resa)
            heure_fin = heure_debut + duree
            
            # Vérifier les chevauchements
            reservations_existantes = Reservation.objects.filter(
                date=date_resa,
                statut__in=['en_attente', 'confirmee']
            ).exclude(id=self.instance.id if self.instance else None)
            
            for reservation in reservations_existantes:
                debut_existant = datetime.combine(reservation.date, reservation.heure)
                fin_existant = debut_existant + timedelta(minutes=reservation.service.duree)
                
                if (heure_debut < fin_existant and heure_fin > debut_existant):
                    raise serializers.ValidationError(
                        {"heure": "Ce créneau n'est pas disponible."}
                    )

        return data

class GalerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galerie
        fields = ['id', 'titre', 'description', 'image', 'date_ajout']
        read_only_fields = ['date_ajout'] 