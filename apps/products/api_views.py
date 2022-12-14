import asyncio
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

from apps.core import client


class ProductApiViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
