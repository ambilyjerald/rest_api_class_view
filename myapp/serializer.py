from dataclasses import fields

from rest_framework import serializers

from myapp.models import employee


class employee_serializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields=('__all__')
