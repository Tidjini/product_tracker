from rest_framework import viewsets


from .models import Encaissement, FactureCharge
from .serializes import EncaissementSerializer, FactureChargeSerializer


class EncaissementViewSet(viewsets.ModelViewSet):

    queryset = Encaissement.objects.all()
    serializer_class = EncaissementSerializer


class FactureChargeViewSet(viewsets.ModelViewSet):

    queryset = FactureCharge.objects.all()
    serializer_class = FactureChargeSerializer
