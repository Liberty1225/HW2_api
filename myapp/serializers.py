from rest_framework import serializers

from .models import Position, Employee


class PositionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    department = serializers.CharField(max_length=30)

    def create(self, validated_data):
        position = Position.objects.create(
            title=validated_data['title'],
            department=validated_data['department'],
        )
        return position


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    birth_year = serializers.DateField()
    salary = serializers.IntegerField(default=0)
    position = PositionSerializer

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)



