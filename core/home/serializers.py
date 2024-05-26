from rest_framework import serializers

from .models import EiinTbl

class EIINSerializer(serializers.ModelSerializer):
    class Meta:
        model = EiinTbl
        fields = ['id', 'eiin', 'code', 'name','district','upazila']