from rest_framework import routers, serializers, viewsets
from .models import Discente
from .serializers import DiscenteSerializer

class DiscenteViewSet(viewsets.ModelViewSet):
    queryset = Discente.objects.all()
    serializer_class = DiscenteSerializer