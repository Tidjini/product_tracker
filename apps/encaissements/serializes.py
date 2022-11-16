from rest_framework import serializers

from .models import Encaissement


class EncaissementSerializer(serializers.ModelSerializer):

    growth_loss = serializers.ReadOnlyField()

    class Meta:
        model = Encaissement
        fields = "__all__"
