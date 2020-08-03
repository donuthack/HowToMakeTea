from rest_framework import serializers
from .models import MakeTea

# class TeaComponents(serializers.Serializer):
#     type = serializers.CharField(max_length=40)
#     water = serializers.IntegerField()
#     temp = serializers.IntegerField()
#     sugar = serializers.IntegerField()


class PrepareTea(serializers.ModelSerializer):
    temp = serializers.IntegerField(min_value=80, max_value=120)
    adds = serializers.ListField(
        child=serializers.CharField(max_length=255)
    )
    water = serializers.IntegerField()
    typeoftea = serializers.CharField()


    class Meta:
        model = MakeTea
        fields = ['temp', 'adds', 'water', 'type_of_tea']
