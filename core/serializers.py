
from rest_framework import serializers
from .models import Discente


class DiscenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discente
        fields = ['id', 'nome', 'email', 'numero', 'ano', 'curso']