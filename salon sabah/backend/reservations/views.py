from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Service, Reservation, Galerie
from .serializers import ServiceSerializer, ReservationSerializer, GalerieSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    def get_permissions(self):
        """
        Permet la création de réservations et la consultation sans authentification,
        mais requiert l'authentification pour les autres opérations
        """
        if self.action in ['create', 'mes_reservations']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'])
    def mes_reservations(self, request):
        """
        Endpoint pour récupérer les réservations d'un client par email
        """
        email = request.query_params.get('email', None)
        if email is None:
            return Response({'error': 'Email parameter is required'}, status=400)
        
        reservations = self.queryset.filter(email=email)
        serializer = self.get_serializer(reservations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def changer_statut(self, request, pk=None):
        """
        Endpoint pour changer le statut d'une réservation
        """
        reservation = get_object_or_404(Reservation, pk=pk)
        nouveau_statut = request.data.get('statut', None)
        
        if nouveau_statut not in dict(Reservation.STATUT_CHOICES):
            return Response({'error': 'Invalid status'}, status=400)
        
        reservation.statut = nouveau_statut
        reservation.save()
        
        serializer = self.get_serializer(reservation)
        return Response(serializer.data)

class GalerieViewSet(viewsets.ModelViewSet):
    queryset = Galerie.objects.all()
    serializer_class = GalerieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
