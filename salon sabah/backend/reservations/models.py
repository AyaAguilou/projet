from django.db import models
from django.core.validators import RegexValidator

class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    duree = models.IntegerField(help_text="Durée en minutes")
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.nom} - {self.prix}€"

class Reservation(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
        ('terminee', 'Terminée'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Le numéro de téléphone doit être au format : '+999999999'"
            )
        ]
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    heure = models.TimeField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    commentaire = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"
        ordering = ['-date', '-heure']

    def __str__(self):
        return f"Réservation de {self.nom} pour {self.service.nom} le {self.date} à {self.heure}"

class Galerie(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='galerie/')
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Photo de la galerie"
        verbose_name_plural = "Galerie photos"
        ordering = ['-date_ajout']

    def __str__(self):
        return self.titre 