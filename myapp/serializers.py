from rest_framework import serializers
from .models import Zapchasti

class ZapchastiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zapchasti
        fields = ('id',
                  'name',
                  'image',
                  'price'
                  )
