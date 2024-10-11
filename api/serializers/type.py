from rest_framework import serializers
from home.models import Type


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'
