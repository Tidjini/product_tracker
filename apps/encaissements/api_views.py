from rest_framework import viewsets


from .models import Encaissement
from .serializes import EncaissementSerializer


class EncaissementViewSet(viewsets.ModelViewSet):

    queryset = Encaissement.objects.all()
    serializer_class = EncaissementSerializer
