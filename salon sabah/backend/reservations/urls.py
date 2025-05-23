from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'services', views.ServiceViewSet)
router.register(r'reservations', views.ReservationViewSet)
router.register(r'galerie', views.GalerieViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 