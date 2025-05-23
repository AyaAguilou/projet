from django.contrib import admin
from .models import Service, Reservation, Galerie

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'duree')
    search_fields = ('nom',)
    list_filter = ('prix', 'duree')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'service', 'date', 'heure', 'statut')
    list_filter = ('statut', 'date', 'service')
    search_fields = ('nom', 'email', 'telephone')
    date_hierarchy = 'date'
    readonly_fields = ('date_creation', 'date_modification')

@admin.register(Galerie)
class GalerieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_ajout')
    search_fields = ('titre', 'description')
    list_filter = ('date_ajout',) 