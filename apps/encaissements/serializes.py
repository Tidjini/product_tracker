from rest_framework import serializers

from .models import Encaissement, FactureCharge, DemandeAchat


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


class DemandeAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeAchat
        fields = "__all__"
        read_only_fileds = ("id",)
