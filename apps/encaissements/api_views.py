from rest_framework import viewsets


from .models import Encaissement, FactureCharge, DemandeAchat
from .serializes import (
    EncaissementSerializer,
    FactureChargeSerializer,
    DemandeAchatSerializer,
)


class EncaissementViewSet(viewsets.ModelViewSet):

    queryset = Encaissement.objects.all()
    serializer_class = EncaissementSerializer


class FactureChargeViewSet(viewsets.ModelViewSet):

    queryset = FactureCharge.objects.all()
    serializer_class = FactureChargeSerializer


class DemandeAchatViewSet(viewsets.ModelViewSet):

    queryset = DemandeAchat.objects.all()
    serializer_class = DemandeAchatSerializer
