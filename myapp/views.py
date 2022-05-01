from rest_framework import viewsets
from .serializers import ZapchastiSerializer
from .models import Zapchasti

class ZapchastiViewSet(viewsets.ModelViewSet):
    queryset = Zapchasti.objects.all().order_by('name')
    serializer_class = ZapchastiSerializer