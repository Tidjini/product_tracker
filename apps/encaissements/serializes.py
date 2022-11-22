from rest_framework import serializers

from .models import Encaissement, FactureCharge


class EncaissementSerializer(serializers.ModelSerializer):

    growth_loss = serializers.ReadOnlyField()

    class Meta:
        model = Encaissement
        fields = "__all__"


class FactureChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactureCharge
        fields = "__all__"
        read_only_fileds = ("id",)
