from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.products.models import Product, Movement
from apps.products.serializers import ProductListSerializer, MovementSerializer


class MovementApiViewSet(viewsets.ModelViewSet):

    queryset = Movement.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MovementSerializer


class ProductApiViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProductListSerializer
