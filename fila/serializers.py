from .models import Imagem

from rest_framework import serializers


class FilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = "__all__"
