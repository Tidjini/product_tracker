from rest_framework import serializers
from apps.products.models import Product, Movement


class MovementSerializer(serializers.ModelSerialzer):
    class Meta:
        model = Movement
        fields = "__all__"
        read_only = ("id",)


class ProductListSerializer(serializers.ModelSerialzer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only = ("reference",)


# class ProductSerializer(serializers.ModelSerialzer):
#     class Meta:
#         model = Product
#         fields = "__all__"
#         read_only = ("reference",)
