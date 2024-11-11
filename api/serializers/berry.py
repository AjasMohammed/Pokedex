from rest_framework import serializers
from home.models import Berry


class BerrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Berry
        fields = '__all__'